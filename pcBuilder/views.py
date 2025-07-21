from django.shortcuts import render
from pcBuilder.models import *
from django.db.models import Prefetch , Q


# Create your views here.


def test(request):
    CPU = get_CPU()

    CPU_gen = next(
        (spec.value for spec in CPU.productspec_set.all() if spec.part_spec.name == "GEN"),
        None
    )
    RAM_GENs = next((spec.value for spec in CPU.productspec_set.all() if spec.part_spec.name == "RAM_GENs"),
        None
    )
    TDP=next(
        (spec.value for spec in CPU.productspec_set.all() if spec.part_spec.name == "TDP"),
        None
    )
    Socket = next(
        (spec.value for spec in CPU.productspec_set.all() if spec.part_spec.name == "Socket"),
        None
    )

    MB=get_MB(CPU_gen,RAM_GENs)

    RAM_GEN_Supported=next(
        (spec.value for spec in MB.productspec_set.all() if spec.part_spec.name == "RAM_GEN_Supported"),
        None
    )

    PCIe_gen = next(
        (spec.value for spec in MB.productspec_set.all() if spec.part_spec.name == "PCIe_GENs"),
        None
    )

    GPU=get_GPU(PCIe_gen)
    RAM=get_RAM(RAM_GEN_Supported)
    Cooler=get_Cooler(TDP,Socket)
    #to do , add the ability of making a build that doesn't need a dedicated GPU


    return render(request,"Home.html",{'CPU':CPU,'MB':MB ,'GPU':GPU,'RAM':RAM,'Cooler':Cooler })




def get_CPU():
    #CPU = Product.objects.filter(part__name="CPU",productspec__part_spec__name="Multicore",price__lte=400).order_by("-productspec__value").first()
    #a=ProductSpec.objects.filter(part_spec__name="Multicore",product__part__name="CPU").filter(product__price__lte=400).order_by("-value").first()
    CPU = Product.objects.filter(
        part__name="CPU",
        productspec__part_spec__name="Multicore"
    ).prefetch_related(
        Prefetch('productspec_set', queryset=ProductSpec.objects.select_related('part_spec'))
    ).order_by('-productspec__value').first()
    return CPU




def get_MB(CPU_gen, RAM_GENs):
    MotherBoard = Product.objects.filter(
        part__name="MotherBoard",
    ).filter(
        Q(productspec__part_spec__name="CPU_GENs_Supported", productspec__value__contains=CPU_gen),

    ).filter(
        #the next line was the main way to do it but for some reason __in doesnt work properly in there. so I had to make a "for" loop to simulate the function of it.
        #Q(productspec__part_spec__name="RAM_GEN_Supported", productspec__value__in=RAM_GENs),

    ).prefetch_related(
        Prefetch('productspec_set', queryset=ProductSpec.objects.select_related('part_spec'))
    ).order_by('-price').distinct()
    #this is the for loop I was talking about
    for motherboard in MotherBoard:
        motherboard_ram_gen=next(
            (spec.value for spec in motherboard.productspec_set.all() if spec.part_spec.name == "RAM_GEN_Supported"),
            None
        )
        if motherboard_ram_gen in RAM_GENs:
            MotherBoard=motherboard
            break
        else:
            MotherBoard=None
    #MotherBoard=MotherBoard.first()
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



