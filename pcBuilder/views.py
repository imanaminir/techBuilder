from itertools import product

from django.shortcuts import render
from django.db.models import Prefetch, Q, IntegerField, Value
from django.db.models.functions import Cast
from pcBuilder.models import *
from collections import Counter




# Create your views here.


def test(request):





    CPU = get_CPU(400)
    # getting the specs in the new way using spec_dict
    CPU_gen =CPU.spec_dict.get("GEN")
    RAM_gens_suported_by_CPU =CPU.spec_dict.get("RAM_GENs")
    CPU_TDP = CPU.spec_dict.get("TDP")
    CPU_Socket=CPU.spec_dict.get("Socket")


    # getting the specs: a query for every spec
    # CPU_gen = ProductSpec.objects.filter(product=CPU, part_spec=PartSpec.objects.get(name="GEN", part__name="CPU")).first()
    # RAM_gens_suported_by_CPU=ProductSpec.objects.filter(product=CPU,part_spec=PartSpec.objects.get(name="RAM_GENs", part__name="CPU")).first()
    #...

    # getting the specs for using prefeatch-related
    # CPU_gen = next(
    #     (spec.value for spec in CPU.productspec_set.all() if spec.part_spec.name == "GEN"),
    #     None
    # )

    # RAM_GENs = next((spec.value for spec in CPU.productspec_set.all() if spec.part_spec.name == "RAM_GENs"),
    #     None
    # )

    # TDP=next(
    #     (spec.value for spec in CPU.productspec_set.all() if spec.part_spec.name == "TDP"),
    #     None
    # )

    # Socket = next(
    #     (spec.value for spec in CPU.productspec_set.all() if spec.part_spec.name == "Socket"),
    #     None
    # )

    MB=get_MB(CPU_gen,RAM_gens_suported_by_CPU)

    PCIe_gen=MB.spec_dict.get("PCIe_GENs")
    ram_slot=MB.spec_dict.get("RAM_GEN_Supported")
    MB_Power_Connector=MB.spec_dict.get("Power_Connector")

    # RAM_GEN_Supported=next(
    #     (spec.value for spec in MB.productspec_set.all() if spec.part_spec.name == "RAM_GEN_Supported"),
    #     None
    # )

    # PCIe_gen = next(
    #     (spec.value for spec in MB.productspec_set.all() if spec.part_spec.name == "PCIe_GENs"),
    #     None
    # )

    GPU=get_GPU(PCIe_gen)

    GPU_power_connector=GPU.spec_dict.get("power_connector")
    GPU_TDP=GPU.spec_dict.get("Power_Needed")

    RAM=get_RAM(ram_slot,32,400)
    Cooler=get_Cooler(CPU_TDP,CPU_Socket)
    # #to do , add the ability of making a build that doesn't need a dedicated GPU
    PSU=get_Power(GPU_power_connector,MB_Power_Connector,CPU_TDP,GPU_TDP)


    return render(request,"Home.html",{'CPU':CPU ,"GPU":GPU ,'MB':MB, 'RAM':RAM[0], 'RAM_num':RAM[1] ,'Cooler':Cooler,'PSU':PSU})





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




def get_MB(CPU_gen, RAM_GENs):
    # Step 1: Get the Part and PartSpecs
    mb_part = Part.objects.get(name="MotherBoard")
    cpu_gen_spec = PartSpec.objects.get(name="CPU_GENs_Supported", part=mb_part)
    ram_gen_spec = PartSpec.objects.get(name="RAM_GEN_Supported", part=mb_part)

    # Step 2: Filter motherboards with matching CPU_GEN and RAM_GEN
    # Find product IDs that support the given CPU gen
    cpu_compatible_mb_ids = ProductSpec.objects.filter(
        part_spec=cpu_gen_spec,
        value__contains=CPU_gen
    ).values_list("product_id", flat=True)
    # Find product IDs that support any of the RAM gens
    ram_mb_ids = ProductSpec.objects.filter(
        part_spec=ram_gen_spec,
        #value__in=["DDR4", "DDR5"]  # assuming value is a single string like "DDR5"
    ).values_list("value","product_id")
    ram_compatible_mb_ids=[]
    for id in ram_mb_ids:
        if id[0] in str(RAM_GENs):
            ram_compatible_mb_ids.append(id[1])

    # Step 3: Intersect the IDs and get the most expensive motherboard
    common_ids = set(cpu_compatible_mb_ids).intersection(ram_compatible_mb_ids)

    MotherBoard = (
        Product.objects
        .filter(id__in=common_ids, part=mb_part, price__lt=400)
        .order_by('-price')
        .first()
    )
    return MotherBoard


def get_GPU(PCIe_gen):
    PCIe_gen.sort()
    PCIe_gen.reverse()
    #GPU = Product.objects.filter(part__name="GPU").first()
    PCIe_gen = PCIe_gen[0]
    supported_versions = {
        "PCIe 5.0": ["PCIe 5.0", "PCIe 4.0", "PCIe 3.0"],
        "PCIe 4.0": ["PCIe 4.0", "PCIe 3.0"],
        "PCIe 3.0": ["PCIe 3.0"]
    }

    supported = supported_versions.get(PCIe_gen, [PCIe_gen])
    GPU = Product.objects.filter(
        part__name="GPU",
        productspec__part_spec__name="PCIe_Gen",
        #productspec__value__in=supported,
        #price__lte=1300
    ).prefetch_related(
        Prefetch('productspec_set', queryset=ProductSpec.objects.select_related('part_spec'))
    ).order_by('-price')

    for gpu in GPU:
        print(gpu.name)
        gpu_pcie=next(
            (spec.value for spec in gpu.productspec_set.all() if spec.part_spec.name == "PCIe_Gen"),
            None
        )
        if gpu_pcie in supported:
            GPU=gpu
            break

        else:
            GPU=None

    return GPU



def get_RAM(RAM_GEN_Supported, needed_capacity, budget):
    ram_part = Part.objects.get(name="RAM")

    # Relevant specs
    gen_spec = PartSpec.objects.get(name="GEN", part=ram_part)
    speed_spec = PartSpec.objects.get(name="Speed", part=ram_part)
    capacity_spec = PartSpec.objects.get(name="Capacity", part=ram_part)
    modules_spec = PartSpec.objects.get(name="Modules_Num", part=ram_part)

    # Get compatible RAMs
    compatible_ram_ids = ProductSpec.objects.filter(
        part_spec=gen_spec,
        value=RAM_GEN_Supported
    ).values_list("product_id", flat=True)

    ram_products = Product.objects.filter(
        id__in=compatible_ram_ids,
        price__lte=budget // 2,  # each stick must be half or less
        part=ram_part
    ).prefetch_related("productspec_set")

    candidates = []

    for ram in ram_products:
        specs = {s.part_spec.name: s.value for s in ram.productspec_set.all()}

        try:
            capacity = int(specs.get("Capacity", 0))     # capacity per module
            modules = int(specs.get("Modules_Num", 1))   # 1 or 2
            speed = int(specs.get("Speed", 0))
            total_capacity = capacity * modules

            # Must use exactly 2 sticks of same product
            combined_capacity = total_capacity * 2
            combined_price = ram.price * 2

            if (
                modules in [1, 2] and
                combined_capacity == needed_capacity and
                combined_price <= budget
            ):
                candidates.append({
                    "product": ram,
                    "count": 2,
                    "total_price": combined_price,
                    "speed": speed,
                })
        except:
            continue  # skip invalid/missing data

    if not candidates:
        return None

    # Sort by highest speed, then lowest total price
    candidates.sort(key=lambda x: (-x["speed"], x["total_price"]))

    return candidates[0]["product"], candidates[0]["count"]




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
    print(connectors_needed)
    PSU=[]

    for psu_connectors in psu_connectors_productspecs:
        print(psu_connectors.product.id)

    print("     ")
    for connectors in psu_connectors_productspecs:

        if is_compatible(connectors_needed,connectors.value):
            print(connectors.product.id)
            PSU.append(connectors.product)




    Power=PSU[0]

    return Power


def is_compatible(required_connectors, psu_connectors):
    required = Counter(required_connectors)
    available = Counter(psu_connectors)

    # مرحله 0: تفسیر کانکتورهای ترکیبی
    # 4+4 EPS می‌تونه به عنوان 8-pin EPS یا دو تا 4-pin EPS عمل کنه
    if '4+4-pin EPS' in available:
        available['8-pin EPS'] += available['4+4-pin EPS']
        available['4-pin EPS'] += available['4+4-pin EPS']
        del available['4+4-pin EPS']

    # 6+2 PCIe می‌تونه به عنوان 8-pin PCIe استفاده بشه
    if '6+2-pin PCIe' in available:
        available['8-pin PCIe'] += available['6+2-pin PCIe']
        del available['6+2-pin PCIe']

    # مرحله 1: تطبیق مستقیم (کانکتورهایی که دقیقاً با هم برابرند)
    for connector in list(required):
        match = min(required[connector], available.get(connector, 0))
        required[connector] -= match
        available[connector] -= match

    # مرحله 2: استفاده از 8-pin EPS برای تأمین 4-pin EPS (در صورت نیاز)
    if required['4-pin EPS'] > 0 and available['8-pin EPS'] > 0:
        match = min(required['4-pin EPS'], available['8-pin EPS'])
        required['4-pin EPS'] -= match
        available['8-pin EPS'] -= match

    # مرحله 3: استفاده از 8-pin PCIe برای GPU (در صورت نیاز)
    if required['8-pin PCIe'] > 0 and available['8-pin PCIe'] > 0:
        match = min(required['8-pin PCIe'], available['8-pin PCIe'])
        required['8-pin PCIe'] -= match
        available['8-pin PCIe'] -= match

    # اگر چیزی در required باقی مونده، یعنی ناسازگاری داریم
    return all(count == 0 for count in required.values())

