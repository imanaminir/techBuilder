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

psu_list = [{'name': 'Corsair HX1200 1200W 80+ Platinum', 'Power (W)': 1200, 'Modularity': 'Fully Modular',
        'Efficiency Rating': '80+ Platinum',
        'Connectors': ['24-pin ATX', '8-pin EPS', '8-pin EPS', '8-pin PCIe', '8-pin PCIe', '8-pin PCIe', '8-pin PCIe',
                       '8-pin PCIe', '8-pin PCIe', 'SATA', 'SATA', 'SATA', 'SATA', 'SATA', 'SATA', 'SATA', 'SATA',
                       'SATA', 'SATA', 'SATA', 'SATA', 'Molex', 'Molex', 'Molex', 'Molex', 'Molex', 'Molex']},
       {'name': 'ASUS ROG Thor 1200W 80+ Platinum II', 'Power (W)': 1200, 'Modularity': 'Fully Modular',
        'Efficiency Rating': '80+ Platinum',
        'Connectors': ['24-pin ATX', '8-pin EPS', '8-pin EPS', '8-pin PCIe', '8-pin PCIe', '8-pin PCIe', '8-pin PCIe',
                       '8-pin PCIe', '8-pin PCIe', 'SATA', 'SATA', 'SATA', 'SATA', 'SATA', 'SATA', 'SATA', 'SATA',
                       'SATA', 'SATA', 'SATA', 'SATA', 'Molex', 'Molex', 'Molex', 'Molex', 'Molex', 'Molex', 'USB-C',
                       '16-pin (12VHPWR)']},
       {'name': 'Seasonic PRIME TX-1000 80+ Titanium', 'Power (W)': 1000, 'Modularity': 'Fully Modular',
        'Efficiency Rating': '80+ Titanium',
        'Connectors': ['24-pin ATX', '8-pin EPS', '8-pin EPS', '8-pin PCIe', '8-pin PCIe', '8-pin PCIe', '8-pin PCIe',
                       '8-pin PCIe', '8-pin PCIe', '8-pin PCIe', '8-pin PCIe', 'SATA', 'SATA', 'SATA', 'SATA', 'SATA',
                       'SATA', 'SATA', 'SATA', 'SATA', 'SATA', 'SATA', 'SATA', 'SATA', 'SATA', 'SATA', 'SATA', 'Molex',
                       'Molex', 'Molex', 'Molex', 'Molex', 'Molex', '16-pin (12VHPWR)']},
       {'name': 'Cooler Master V1300 Platinum', 'Power (W)': 1300, 'Modularity': 'Fully Modular',
        'Efficiency Rating': '80+ Platinum',
        'Connectors': ['24-pin ATX', '8-pin EPS', '8-pin EPS', '8-pin PCIe', '8-pin PCIe', '8-pin PCIe', '8-pin PCIe',
                       '8-pin PCIe', '8-pin PCIe', 'SATA', 'SATA', 'SATA', 'SATA', 'SATA', 'SATA', 'SATA', 'SATA',
                       'SATA', 'SATA', 'SATA', 'SATA', 'Molex', 'Molex', 'Molex', 'Molex', 'Molex', 'Molex',
                       '16-pin (12VHPWR)']},
       {'name': 'Thermaltake Toughpower PF1 ARGB 1200W', 'Power (W)': 1200, 'Modularity': 'Fully Modular',
        'Efficiency Rating': '80+ Platinum',
        'Connectors': ['24-pin ATX', '8-pin EPS', '8-pin EPS', '8-pin PCIe', '8-pin PCIe', '8-pin PCIe', '8-pin PCIe',
                       '8-pin PCIe', '8-pin PCIe', 'SATA', 'SATA', 'SATA', 'SATA', 'SATA', 'SATA', 'SATA', 'SATA',
                       'SATA', 'SATA', 'SATA', 'SATA', 'Molex', 'Molex', 'Molex', 'Molex', 'Molex', 'Molex',
                       'ARGB Header', '16-pin (12VHPWR)']},
       {'name': 'Corsair RM850x 850W 80+ Gold Fully Modular', 'Power (W)': 850, 'Modularity': 'Fully Modular',
        'Efficiency Rating': '80+ Gold',
        'Connectors': ['24-pin ATX', '8-pin EPS', '8-pin EPS', '8-pin PCIe', '8-pin PCIe', '8-pin PCIe', '8-pin PCIe',
                       'SATA', 'SATA', 'SATA', 'SATA', 'SATA', 'SATA', 'SATA', 'SATA', 'Molex', 'Molex', 'Molex',
                       'Molex']},
       {'name': 'Seasonic FOCUS GX-850 850W 80+ Gold', 'Power (W)': 850, 'Modularity': 'Fully Modular',
        'Efficiency Rating': '80+ Gold',
        'Connectors': ['24-pin ATX', '8-pin EPS', '8-pin EPS', '8-pin PCIe', '8-pin PCIe', '8-pin PCIe', '8-pin PCIe',
                       'SATA', 'SATA', 'SATA', 'SATA', 'SATA', 'SATA', 'SATA', 'SATA', 'Molex', 'Molex', 'Molex',
                       'Molex']},
       {'name': 'ASUS ROG Thor 850W 80+ Platinum', 'Power (W)': 850, 'Modularity': 'Fully Modular',
        'Efficiency Rating': '80+ Platinum',
        'Connectors': ['24-pin ATX', '8-pin EPS', '8-pin EPS', '8-pin PCIe', '8-pin PCIe', '8-pin PCIe', '8-pin PCIe',
                       'SATA', 'SATA', 'SATA', 'SATA', 'SATA', 'SATA', 'SATA', 'SATA', 'Molex', 'Molex', 'Molex',
                       'Molex', 'OLED Display', '16-pin (12VHPWR)']},
       {'name': 'Cooler Master V850 Gold V2', 'Power (W)': 850, 'Modularity': 'Fully Modular',
        'Efficiency Rating': '80+ Gold',
        'Connectors': ['24-pin ATX', '8-pin EPS', '8-pin EPS', '8-pin PCIe', '8-pin PCIe', '8-pin PCIe', '8-pin PCIe',
                       'SATA', 'SATA', 'SATA', 'SATA', 'SATA', 'SATA', 'SATA', 'SATA', 'Molex', 'Molex', 'Molex',
                       'Molex', '16-pin (12VHPWR)']},
       {'name': 'Thermaltake Toughpower GF1 850W', 'Power (W)': 850, 'Modularity': 'Fully Modular',
        'Efficiency Rating': '80+ Gold',
        'Connectors': ['24-pin ATX', '8-pin EPS', '8-pin EPS', '8-pin PCIe', '8-pin PCIe', '8-pin PCIe', '8-pin PCIe',
                       'SATA', 'SATA', 'SATA', 'SATA', 'SATA', 'SATA', 'SATA', 'SATA', 'Molex', 'Molex', 'Molex',
                       'Molex']},
       {'name': 'Corsair CX650M 650W 80+ Bronze Semi-Modular', 'Power (W)': 650, 'Modularity': 'Semi-Modular',
        'Efficiency Rating': '80+ Bronze',
        'Connectors': ['24-pin ATX', '8-pin EPS', '8-pin PCIe', '8-pin PCIe', 'SATA', 'SATA', 'SATA', 'SATA', 'SATA',
                       'SATA', 'Molex', 'Molex', 'Molex']},
       {'name': 'Cooler Master MWE Bronze V2 650W', 'Power (W)': 650, 'Modularity': 'Non-Modular',
        'Efficiency Rating': '80+ Bronze',
        'Connectors': ['24-pin ATX', '8-pin EPS', '8-pin PCIe', '8-pin PCIe', 'SATA', 'SATA', 'SATA', 'SATA', 'SATA',
                       'SATA', 'Molex', 'Molex', 'Molex']},
       {'name': 'EVGA 600 BR 600W 80+ Bronze', 'Power (W)': 600, 'Modularity': 'Non-Modular',
        'Efficiency Rating': '80+ Bronze',
        'Connectors': ['24-pin ATX', '8-pin EPS', '8-pin PCIe', '8-pin PCIe', 'SATA', 'SATA', 'SATA', 'SATA', 'SATA',
                       'SATA', 'Molex', 'Molex', 'Molex']},
       {'name': 'Thermaltake Smart BX1 650W', 'Power (W)': 650, 'Modularity': 'Non-Modular',
        'Efficiency Rating': '80+ Bronze',
        'Connectors': ['24-pin ATX', '8-pin EPS', '8-pin PCIe', '8-pin PCIe', 'SATA', 'SATA', 'SATA', 'SATA', 'SATA',
                       'SATA', 'Molex', 'Molex', 'Molex']},
       {'name': 'ASUS TUF Gaming 650B 650W', 'Power (W)': 650, 'Modularity': 'Non-Modular',
        'Efficiency Rating': '80+ Bronze',
        'Connectors': ['24-pin ATX', '8-pin EPS', '8-pin PCIe', '8-pin PCIe', 'SATA', 'SATA', 'SATA', 'SATA', 'SATA',
                       'SATA', 'Molex', 'Molex', 'Molex']},
       {'name': 'Cooler Master Elite V3 500W', 'Power (W)': 500, 'Modularity': 'Non-Modular',
        'Efficiency Rating': '80+',
        'Connectors': ['24-pin ATX', '4+4-pin EPS', '8-pin PCIe', 'SATA', 'SATA', 'SATA', 'SATA', 'Molex', 'Molex']},
       {'name': 'Thermaltake Smart Series 500W', 'Power (W)': 500, 'Modularity': 'Non-Modular',
        'Efficiency Rating': '80+',
        'Connectors': ['24-pin ATX', '4+4-pin EPS', '8-pin PCIe', 'SATA', 'SATA', 'SATA', 'SATA', 'Molex', 'Molex']},
       {'name': 'Corsair CV550 550W', 'Power (W)': 550, 'Modularity': 'Non-Modular', 'Efficiency Rating': '80+ Bronze',
        'Connectors': ['24-pin ATX', '4+4-pin EPS', '8-pin PCIe', 'SATA', 'SATA', 'SATA', 'SATA', 'Molex', 'Molex']},
       {'name': 'Gigabyte P450B 450W', 'Power (W)': 450, 'Modularity': 'Non-Modular', 'Efficiency Rating': '80+ Bronze',
        'Connectors': ['24-pin ATX', '4+4-pin EPS', '6+2-pin PCIe', 'SATA', 'SATA', 'SATA', 'SATA', 'Molex', 'Molex']},
       {'name': 'DeepCool DN500 500W', 'Power (W)': 500, 'Modularity': 'Non-Modular', 'Efficiency Rating': '80+',
        'Connectors': ['24-pin ATX', '4+4-pin EPS', '6+2-pin PCIe', 'SATA', 'SATA', 'SATA', 'SATA', 'Molex', 'Molex']}]
