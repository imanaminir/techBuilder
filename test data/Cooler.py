import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'techBuilder.settings')
django.setup()

from pcBuilder.models import Product, Part, PartSpec,ProductSpec
Part.objects.get_or_create(name="Cooler")
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
    Product.objects.get_or_create(
        name=Cooler["name"],
        part=Cooler_part,
        brand=Cooler["brand"],
        price=Cooler["price"]
    )


coolers_specs = [
    # AIO Liquid Coolers
    {
        "name": "Corsair iCUE H100i RGB Elite 240mm",
        "type": "AIO Liquid",
        "tdp_capacity": 250,
        "compatible_sockets": ["Intel LGA1700", "Intel LGA1200", "Intel LGA115x", "AMD AM5", "AMD AM4"]
    },
    {
        "name": "NZXT Kraken X53 RGB 240mm",
        "type": "AIO Liquid",
        "tdp_capacity": 240,
        "compatible_sockets": ["Intel LGA1700", "Intel LGA1200", "Intel LGA115x", "AMD AM5", "AMD AM4"]
    },
    {
        "name": "Cooler Master MasterLiquid ML240L V2",
        "type": "AIO Liquid",
        "tdp_capacity": 200,
        "compatible_sockets": ["Intel LGA1700", "Intel LGA1200", "Intel LGA115x", "AMD AM5", "AMD AM4"]
    },
    {
        "name": "DeepCool LS520 240mm",
        "type": "AIO Liquid",
        "tdp_capacity": 260,
        "compatible_sockets": ["Intel LGA1700", "Intel LGA1200", "Intel LGA115x", "AMD AM5", "AMD AM4"]
    },
    {
        "name": "ARCTIC Liquid Freezer II 240mm",
        "type": "AIO Liquid",
        "tdp_capacity": 270,
        "compatible_sockets": ["Intel LGA1700", "Intel LGA1200", "Intel LGA115x", "AMD AM5", "AMD AM4"]
    },
    {
        "name": "Thermaltake TH360 ARGB Sync 360mm",
        "type": "AIO Liquid",
        "tdp_capacity": 280,
        "compatible_sockets": ["Intel LGA1700", "Intel LGA1200", "Intel LGA115x", "AMD AM5", "AMD AM4"]
    },
    {
        "name": "Lian Li Galahad II Trinity 240mm",
        "type": "AIO Liquid",
        "tdp_capacity": 275,
        "compatible_sockets": ["Intel LGA1700", "Intel LGA1200", "Intel LGA115x", "AMD AM5", "AMD AM4"]
    },

    # Air Coolers
    {
        "name": "Cooler Master Hyper 212 Black Edition",
        "type": "Air",
        "tdp_capacity": 150,
        "compatible_sockets": ["Intel LGA1700", "Intel LGA1200", "Intel LGA115x", "AMD AM5", "AMD AM4"]
    },
    {
        "name": "DeepCool GAMMAXX 400 V2",
        "type": "Air",
        "tdp_capacity": 130,
        "compatible_sockets": ["Intel LGA1700", "Intel LGA1200", "Intel LGA115x", "AMD AM5", "AMD AM4"]
    },
    {
        "name": "be quiet! Pure Rock 2 Black",
        "type": "Air",
        "tdp_capacity": 150,
        "compatible_sockets": ["Intel LGA1700", "Intel LGA1200", "Intel LGA115x", "AMD AM5", "AMD AM4"]
    },
    {
        "name": "Noctua NH-U12S Redux",
        "type": "Air",
        "tdp_capacity": 180,
        "compatible_sockets": ["Intel LGA1700", "Intel LGA1200", "Intel LGA115x", "AMD AM5", "AMD AM4"]
    },
    {
        "name": "Thermalright Assassin X 120 SE",
        "type": "Air",
        "tdp_capacity": 160,
        "compatible_sockets": ["Intel LGA1700", "Intel LGA1200", "Intel LGA115x", "AMD AM5", "AMD AM4"]
    },
    {
        "name": "ARCTIC Freezer 34 eSports DUO",
        "type": "Air",
        "tdp_capacity": 170,
        "compatible_sockets": ["Intel LGA1700", "Intel LGA1200", "Intel LGA115x", "AMD AM5", "AMD AM4"]
    },
    {
        "name": "Vetroo V5 Black",
        "type": "Air",
        "tdp_capacity": 140,
        "compatible_sockets": ["Intel LGA1700", "Intel LGA1200", "Intel LGA115x", "AMD AM5", "AMD AM4"]
    }
]

PartSpec.objects.get_or_create(name="type",part=Cooler_part)
PartSpec.objects.get_or_create(name="tdp_capacity",part=Cooler_part)
PartSpec.objects.get_or_create(name="compatible_sockets",part=Cooler_part)



type=PartSpec.objects.get(name="type",part=Cooler_part)
tdp_capacity=PartSpec.objects.get(name="tdp_capacity",part=Cooler_part)
compatible_sockets=PartSpec.objects.get(name="compatible_sockets",part=Cooler_part)



for product in coolers_specs:
    THEproduct=Product.objects.get(name=product["name"])
    ProductSpec.objects.get_or_create(product=THEproduct,part_spec=type,value=product["type"])
    ProductSpec.objects.get_or_create(product=THEproduct, part_spec=tdp_capacity, value=product["tdp_capacity"])
    ProductSpec.objects.get_or_create(product=THEproduct, part_spec=compatible_sockets, value=product["compatible_sockets"])



