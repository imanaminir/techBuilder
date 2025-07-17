from itertools import product

from django.shortcuts import render
from django.http import HttpResponse
from pcBuilder.models import *
from django.db.models.functions import Cast
from django.db.models import IntegerField

# Create your views here.


def test(request):
    CPU = get_CPU()
    CPU_GEN=ProductSpec.objects.filter(product=CPU,part_spec__name="GEN").first().value
    MB=get_MB(CPU_GEN)
    return HttpResponse(MB)

def get_CPU():
    CPU = Product.objects.filter(part__name="CPU",productspec__part_spec__name="Multicore",price__lte=400).order_by("-productspec__value").first()
    #a=ProductSpec.objects.filter(part_spec__name="Multicore",product__part__name="CPU").filter(product__price__lte=400).order_by("-value").first()

    return CPU

def get_MB(CPU_GEN):

    MotherBoard = ProductSpec.objects.filter(part_spec__name="CPU_GENs_Supported",product__part__name__iexact="Motherboard",value__contains=CPU_GEN).select_related("product").order_by("product__price").first().product

    return str(MotherBoard)


def get_GPU():
    GPU = Product.objects.filter(part__name="GPU").first()

    return str(GPU)


def get_RAM():
    RAM = Product.objects.filter(part__name="RAM").first()

    return str(RAM)


def get_Cooler():
    Cooler = Product.objects.filter(part__name="Cooler").first()

    return str(Cooler)


def get_Power():
    Power = Product.objects.filter(part__name="Power").first()

    return str(Power)



