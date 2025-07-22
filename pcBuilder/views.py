from django.shortcuts import render
from django.db.models import Prefetch, Q, IntegerField, Value
from django.db.models.functions import Cast
from pcBuilder.models import *



# Create your views here.


def test(request):



    CPU = get_CPU()
    # getting the specs in the new way using spec_dict
    CPU_gen =CPU.spec_dict.get("GEN")
    RAM_gens_suported_by_CPU =CPU.spec_dict.get("RAM_GENs")
    TDP = CPU.spec_dict.get("TDP")
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



    # RAM_GEN_Supported=next(
    #     (spec.value for spec in MB.productspec_set.all() if spec.part_spec.name == "RAM_GEN_Supported"),
    #     None
    # )

    # PCIe_gen = next(
    #     (spec.value for spec in MB.productspec_set.all() if spec.part_spec.name == "PCIe_GENs"),
    #     None
    # )

    # GPU=get_GPU(PCIe_gen)
    # RAM=get_RAM(RAM_GEN_Supported)
    # Cooler=get_Cooler(TDP,Socket)
    # #to do , add the ability of making a build that doesn't need a dedicated GPU


    return render(request,"Home.html",{'CPU':CPU ,"RAM_gens_suported_by_CPU":RAM_gens_suported_by_CPU ,'MB':MB })




def get_CPU():
    cpu_part = Part.objects.get(name="CPU")
    multicore_spec = PartSpec.objects.get(name="Multicore", part=cpu_part)

    CPU = (
        ProductSpec.objects
        .filter(part_spec=multicore_spec, product__part=cpu_part, product__price__lt=400)
        .annotate(multicore_value=Cast('value', IntegerField()))
        .order_by('-multicore_value')
        .select_related('product').first()
    )
    return CPU.product


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


def get_RAM(RAM_GEN_Supported):
    RAM = (Product.objects.filter(
        Q(productspec__part_spec__name="GEN",
        productspec__value=RAM_GEN_Supported,)
    ).filter(
        part__name="RAM",
        productspec__part_spec__name="Speed",
        #productspec__value__gt=1,
    ).prefetch_related(
        Prefetch('productspec_set', queryset=ProductSpec.objects.select_related('part_spec'))
    ).order_by('-productspec__value','-price').first())
    return RAM


def get_Cooler(TDP,CPU_Socket):

    Cooler = Product.objects.filter(

    ).filter(
        Q(
            part__name="Cooler",
            productspec__part_spec__name="compatible_sockets",
            productspec__value__contains=CPU_Socket
          ),

        Q(
            productspec__part_spec__name="tdp_capacity",
            productspec__value__gt=TDP
          )
    ).prefetch_related(
        Prefetch('productspec_set', queryset=ProductSpec.objects.select_related('part_spec'))
    ).order_by("productspec__value","-price").first

    # for cooler in Cooler :
    #     tdp_capacity= next(
    #         (spec.value for spec in cooler.productspec_set.all() if spec.part_spec.name == "tdp_capacity"),
    #         None
    #     )
    #     if TDP <= tdp_capacity:
    #         Cooler=cooler
    #         break
    #     else:
    #         Cooler=None

    return Cooler


def get_Power():
    Power = Product.objects.filter(part__name="Power").first()

    return str(Power)



