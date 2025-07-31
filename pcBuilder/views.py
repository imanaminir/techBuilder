from itertools import product

from django.shortcuts import render
from django.db.models import Prefetch, Q, IntegerField, Value
from django.db.models.functions import Cast
from pcBuilder.models import *
from collections import Counter





# Create your views here.


def test(request):

    inputs={
        "CPU_budget":600,
        "MotherBoard_budget":300,
        "GPU_budget":200,
        "RAM_budget": 300,
        "RAM_capacity": 32,

    }

    CPU = get_CPU(inputs["CPU_budget"])

    # getting the specs in the new way using spec_dict
    CPU_gen =CPU.spec_dict.get("GEN")
    RAM_gens_suported_by_CPU =CPU.spec_dict.get("RAM_GENs")
    CPU_TDP = CPU.spec_dict.get("TDP")
    CPU_Socket=CPU.spec_dict.get("Socket")
    CPU_price=CPU.price



    MB=get_MB(CPU_gen,RAM_gens_suported_by_CPU,inputs["MotherBoard_budget"])

    PCIe_gen=MB.spec_dict.get("PCIe_GENs")
    ram_slot=MB.spec_dict.get("RAM_GEN_Supported")
    MB_Power_Connector=MB.spec_dict.get("Power_Connector")
    MB_price=MB.price



    #to do , add the ability of making a build that doesn't need a dedicated GPU
    GPU=get_GPU(PCIe_gen,inputs["GPU_budget"])

    GPU_power_connector=GPU.spec_dict.get("power_connector")
    GPU_TDP=GPU.spec_dict.get("Power_Needed")
    GPU_price=GPU.price



    RAM=get_RAM(ram_slot,inputs["RAM_capacity"],inputs["RAM_budget"])
    RAM_price=RAM[0].price*RAM[1]



    Cooler=get_Cooler(CPU_TDP,CPU_Socket)
    Cooler_price=Cooler.price



    PSU=get_Power(GPU_power_connector,MB_Power_Connector,CPU_TDP,GPU_TDP)
    PSU_price=PSU.price

    return render(request,"Home.html",{
        'CPU':CPU,'CPU_price':CPU_price ,
        "GPU":GPU ,'GPU_price':GPU_price,
        'MB':MB,'MB_price':MB_price,
        'RAM':RAM[0], 'RAM_num':RAM[1] ,'RAM_price':RAM_price,
        'Cooler':Cooler,'Cooler_price':Cooler_price,
        'PSU':PSU,'PSU_price':PSU_price,
    })





def get_CPU(budget):
    cpu_part = Part.objects.get(name="CPU")
    multicore_spec = PartSpec.objects.get(name="Multicore", part=cpu_part)

    best_cpu_spec = (
        ProductSpec.objects
        .filter(part_spec=multicore_spec, product__part=cpu_part, product__price__lt=budget)
        .annotate(multicore_value=Cast('value', IntegerField()))
        .order_by('-multicore_value')
        .select_related('product')
        .first()
    )

    return best_cpu_spec.product if best_cpu_spec else None




def get_MB(CPU_gen, RAM_GENs, budget):
    mb_part = Part.objects.get(name="MotherBoard")
    cpu_gen_spec = PartSpec.objects.get(name="CPU_GENs_Supported", part=mb_part)
    ram_gen_spec = PartSpec.objects.get(name="RAM_GEN_Supported", part=mb_part)

    # Motherboards that support the CPU gen
    cpu_compatible_mb_ids = ProductSpec.objects.filter(
        part_spec=cpu_gen_spec,
        value__contains=CPU_gen
    ).values_list("product_id", flat=True)

    # Motherboards that support any of the desired RAM gens
    ram_mb_qs = ProductSpec.objects.filter(
        part_spec=ram_gen_spec
    ).values_list("value", "product_id")

    ram_compatible_mb_ids = [
        product_id for value, product_id in ram_mb_qs if value in RAM_GENs
    ]

    # Intersection of both conditions
    compatible_ids = set(cpu_compatible_mb_ids).intersection(ram_compatible_mb_ids)

    motherboard = (
        Product.objects
        .filter(id__in=compatible_ids, part=mb_part, price__lte=budget)
        .order_by('-price')
        .first()
    )

    return motherboard



def get_GPU(PCIe_gen, budget):
    # Sort and prioritize highest generation
    PCIe_gen.sort(reverse=True)
    target_gen = PCIe_gen[0]

    # Define backward-compatible supported generations
    supported_versions = {
        "PCIe 5.0": ["PCIe 5.0", "PCIe 4.0", "PCIe 3.0"],
        "PCIe 4.0": ["PCIe 4.0", "PCIe 3.0"],
        "PCIe 3.0": ["PCIe 3.0"],
    }

    supported = supported_versions.get(target_gen, [target_gen])

    # Get GPU products under budget
    gpu_qs = Product.objects.filter(
        part__name="GPU",
        price__lte=budget,
        productspec__part_spec__name="PCIe_Gen"
    ).prefetch_related(
        Prefetch('productspec_set', queryset=ProductSpec.objects.select_related('part_spec'))
    ).order_by('-price')  # Most expensive first

    # Choose the first GPU with compatible PCIe Gen
    for gpu in gpu_qs:
        gpu_pcie = next(
            (spec.value for spec in gpu.productspec_set.all() if spec.part_spec.name == "PCIe_Gen"),
            None
        )
        if gpu_pcie in supported:
            return gpu  # First compatible one (most expensive)

    return None  # No compatible GPU found



def get_RAM(RAM_GEN_Supported, needed_capacity, budget):
    ram_part = Part.objects.get(name="RAM")

    # Relevant specs
    gen_spec = PartSpec.objects.get(name="GEN", part=ram_part)
    speed_spec = PartSpec.objects.get(name="Speed", part=ram_part)
    capacity_spec = PartSpec.objects.get(name="Capacity", part=ram_part)
    modules_spec = PartSpec.objects.get(name="Modules_Num", part=ram_part)

    # Get compatible RAMs (match GEN as string or list)
    compatible_ram_ids = ProductSpec.objects.filter(
        part_spec=gen_spec,
        value__contains=RAM_GEN_Supported
    ).values_list("product_id", flat=True)

    ram_products = Product.objects.filter(
        id__in=compatible_ram_ids,
        price__lte=budget,
        part=ram_part
    ).prefetch_related("productspec_set")

    candidates = []

    for ram in ram_products:
        specs = {s.part_spec.name: s.value for s in ram.productspec_set.all()}

        try:
            capacity = int(specs.get("Capacity", 0))     # per product
            modules = int(specs.get("Modules_Num", 1))   # 1 or 2
            speed = int(specs.get("Speed", 0))

            # ✅ Try 2 identical products
            total_capacity_2 = capacity * 2
            total_price_2 = ram.price * 2
            total_modules_2 = modules * 2

            if (
                total_modules_2 <= 2 and
                total_price_2 <= budget and
                total_capacity_2 >= needed_capacity
            ):
                candidates.append({
                    "product": ram,
                    "count": 2,
                    "total_price": total_price_2,
                    "capacity": total_capacity_2,
                    "speed": speed,
                })
                continue  # prefer 2-stick if valid

            # ✅ Try 1 product
            total_capacity_1 = capacity
            total_price_1 = ram.price
            total_modules_1 = modules

            if (
                total_modules_1 <= 2 and
                total_price_1 <= budget and
                total_capacity_1 >= needed_capacity
            ):
                candidates.append({
                    "product": ram,
                    "count": 1,
                    "total_price": total_price_1,
                    "capacity": total_capacity_1,
                    "speed": speed,
                })

        except (ValueError, TypeError):
            continue  # skip malformed or missing values

    if not candidates:
        return None

    # ✅ Sort by: exact capacity match > lowest price > highest speed
    candidates.sort(key=lambda x: (
        abs(x["capacity"] - needed_capacity),  # prioritize exact match
        x["total_price"],                     # then cheaper
        -x["speed"]                           # then faster
    ))

    best = candidates[0]
    return best["product"], best["count"]




def get_Cooler(TDP,CPU_Socket):

    cooler_part=Part.objects.get(name="Cooler")
    cooler_tdp_spec=PartSpec.objects.get(name="tdp_capacity", part=cooler_part)
    cpu_sockets_compatible=PartSpec.objects.get(name="compatible_sockets", part=cooler_part)


    compatible_cpus_by_socket_ids=ProductSpec.objects.filter(
        part_spec=cpu_sockets_compatible,
        value__contains=CPU_Socket
    ).values_list("product_id", flat=True)


    compatible_cooles=ProductSpec.objects.filter(
        part_spec=cooler_tdp_spec,
    ).values_list("product_id", 'value')

    cp_COOL=[]
    for id in compatible_cooles:
        if id[1] > TDP:
            cp_COOL.append(id[0])


    Cooler=(ProductSpec.objects.filter(
        part_spec=cooler_tdp_spec,
        product__id__in=cp_COOL,
        product__price__lt=400)
    .annotate(TDP=Cast('value', IntegerField()))
    .order_by('product__price','TDP')
    .select_related('product').first()
    )
    return Cooler.product


def get_Power(GPU_connector,MB_connector,CPU_TDP,GPU_TDP):
    psu_part=Part.objects.get(name="Power")
    psu_power_spec=PartSpec.objects.get(name="Power", part=psu_part)
    psu_connectors_spec=PartSpec.objects.get(name="Connectors", part=psu_part)


    psu_ids_powers=ProductSpec.objects.filter(
        part_spec=psu_power_spec,

    ).values_list("product_id",'value')


    enough_power_psu_ids=[]
    power_need=(CPU_TDP+GPU_TDP+125) * 1.2
    for power in psu_ids_powers:
        if power[1] > power_need:
            enough_power_psu_ids.append(power[0])



    psu_connectors_productspecs=ProductSpec.objects.filter(
        part_spec=psu_connectors_spec,
        product__id__in=enough_power_psu_ids,

    ).order_by("product__price").select_related('product')

    connectors_needed=GPU_connector+MB_connector
    PSU=[]

    for connectors in psu_connectors_productspecs:

        if can_power(connectors_needed,connectors.value):
            PSU.append(connectors.product)

    Power=PSU[0]

    return Power


def normalize_connector(connector):
    """تبدیل کانکتورهای ترکیبی به شکل قابل استفاده"""
    if connector in ['4+4-pin EPS', '8-pin EPS']:
        return ['4-pin EPS', '4-pin EPS']
    elif connector in ['6+2-pin PCIe', '8-pin PCIe']:
        return ['6-pin PCIe', '2-pin PCIe']
    elif connector in ['6-pin PCIe', '2-pin PCIe', '4-pin EPS', '24-pin ATX', 'SATA', 'Molex']:
        return [connector]
    else:
        return []

def can_power(required, available):
    # ایجاد شمارش از کانکتورهای موجود روی پاور
    available_expanded = []
    for conn in available:
        available_expanded.extend(normalize_connector(conn))
    available_counter = Counter(available_expanded)

    # بررسی تک تک کانکتورهای موردنیاز
    for req in required:
        required_parts = normalize_connector(req)

        for part in required_parts:
            if available_counter[part] > 0:
                available_counter[part] -= 1
            else:
                return False  # اگر یک بخش از کانکتور قابل تأمین نباشد، false برمی‌گردد

    return True



