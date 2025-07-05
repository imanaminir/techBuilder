import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'techBuilder.settings')
django.setup()

from pcBuilder.models import Product, Part
Part.objects.create(name="Cooler")
Cooler_part = Part.objects.get(name="Cooler")


Coolers=[
    {"name": "Corsair iCUE H100i RGB Elite 240mm", "brand": "Corsair", "price": 109},
    {"name": "NZXT Kraken X53 RGB 240mm", "brand": "NZXT", "price": 129},
    {"name": "Cooler Master MasterLiquid ML240L V2", "brand": "Cooler Master", "price": 89},
    {"name": "DeepCool LS520 240mm", "brand": "DeepCool", "price": 89},
    {"name": "ARCTIC Liquid Freezer II 240mm", "brand": "ARCTIC", "price": 99},
    {"name": "Thermaltake TH360 ARGB Sync 360mm", "brand": "Thermaltake", "price": 139},
    {"name": "Lian Li Galahad II Trinity 240mm", "brand": "Lian Li", "price": 119},



    {"name": "Cooler Master Hyper 212 Black Edition", "brand": "Cooler Master", "price": 39},
    {"name": "DeepCool GAMMAXX 400 V2", "brand": "DeepCool", "price": 28},
    {"name": "be quiet! Pure Rock 2 Black", "brand": "be quiet!", "price": 45},
    {"name": "Noctua NH-U12S Redux", "brand": "Noctua", "price": 49},
    {"name": "Thermalright Assassin X 120 SE", "brand": "Thermalright", "price": 29},
    {"name": "ARCTIC Freezer 34 eSports DUO", "brand": "ARCTIC", "price": 39},
    {"name": "Vetroo V5 Black", "brand": "Vetroo", "price": 25}

]




for Cooler in Coolers:
    Product.objects.create(
        name=Cooler["name"],
        part=Cooler_part,
        brand=Cooler["brand"],
        price=Cooler["price"]
    )