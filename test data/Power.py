import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'techBuilder.settings')
django.setup()

from pcBuilder.models import Product, Part
Part.objects.create(name="Power")
Power_part = Part.objects.get(name="Power")


Powers=[


    {"name": "Corsair HX1200 1200W 80+ Platinum", "brand": "Corsair", "price": 229},
    {"name": "ASUS ROG Thor 1200W 80+ Platinum II", "brand": "ASUS", "price": 299},
    {"name": "Seasonic PRIME TX-1000 80+ Titanium", "brand": "Seasonic", "price": 279},
    {"name": "Cooler Master V1300 Platinum", "brand": "Cooler Master", "price": 289},
    {"name": "Thermaltake Toughpower PF1 ARGB 1200W", "brand": "Thermaltake", "price": 249},

    {"name": "Corsair RM850x 850W 80+ Gold Fully Modular", "brand": "Corsair", "price": 119},
    {"name": "Seasonic FOCUS GX-850 850W 80+ Gold", "brand": "Seasonic", "price": 129},
    {"name": "ASUS ROG Thor 850W 80+ Platinum", "brand": "ASUS", "price": 199},
    {"name": "Cooler Master V850 Gold V2", "brand": "Cooler Master", "price": 139},
    {"name": "Thermaltake Toughpower GF1 850W", "brand": "Thermaltake", "price": 129},

    {"name": "Corsair CX650M 650W 80+ Bronze Semi-Modular", "brand": "Corsair", "price": 74},
    {"name": "Cooler Master MWE Bronze V2 650W", "brand": "Cooler Master", "price": 69},
    {"name": "EVGA 600 BR 600W 80+ Bronze", "brand": "EVGA", "price": 59},
    {"name": "Thermaltake Smart BX1 650W", "brand": "Thermaltake", "price": 65},
    {"name": "ASUS TUF Gaming 650B 650W", "brand": "ASUS", "price": 72},

    {"name": "Cooler Master Elite V3 500W", "brand": "Cooler Master", "price": 39},
    {"name": "Thermaltake Smart Series 500W", "brand": "Thermaltake", "price": 42},
    {"name": "Corsair CV550 550W", "brand": "Corsair", "price": 49},
    {"name": "Gigabyte P450B 450W", "brand": "Gigabyte", "price": 45},
    {"name": "DeepCool DN500 500W", "brand": "DeepCool", "price": 38}

]


for Power in Powers:
    Product.objects.create(
        name=Power["name"],
        part=Power_part,
        brand=Power["brand"],
        price=Power["price"]
    )