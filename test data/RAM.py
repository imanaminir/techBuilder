import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'techBuilder.settings')
django.setup()

from pcBuilder.models import Product, Part, PartSpec,ProductSpec
Part.objects.get_or_create(name="RAM")
RAM_part = Part.objects.get(name="RAM")

RAMs=[
    {"name": "Corsair Vengeance DDR5 32GB (2x16GB) 6000MHz CL36", "brand": "Corsair", "price": 349},
    {"name": "Corsair Dominator Platinum RGB DDR5 32GB 6400MHz", "brand": "Corsair", "price": 439},
    {"name": "Corsair Vengeance DDR5 16GB (1x16GB) 5600MHz", "brand": "Corsair", "price": 179},

    {"name": "G.Skill Trident Z5 RGB DDR5 32GB (2x16GB) 6000MHz", "brand": "G.Skill", "price": 369},
    {"name": "G.Skill Ripjaws S5 DDR5 32GB 5600MHz CL36", "brand": "G.Skill", "price": 309},
    {"name": "G.Skill Trident Z5 RGB DDR5 64GB (2x32GB) 6400MHz", "brand": "G.Skill", "price": 679},

    {"name": "Kingston FURY Beast DDR5 32GB (2x16GB) 6000MT/s", "brand": "Kingston", "price": 329},
    {"name": "Kingston FURY Beast RGB DDR5 16GB 5600MT/s", "brand": "Kingston", "price": 169},
    {"name": "Kingston FURY Renegade DDR5 32GB 6400MT/s", "brand": "Kingston", "price": 389},

    {"name": "Crucial DDR5 32GB (2x16GB) 5600MT/s", "brand": "Crucial", "price": 279},
    {"name": "Crucial DDR5 16GB 5200MT/s", "brand": "Crucial", "price": 139},

    {"name": "TeamGroup T-Force Delta RGB DDR5 32GB 6000MHz", "brand": "TeamGroup", "price": 319},
    {"name": "TeamGroup T-Force Vulcan DDR5 32GB 5600MHz", "brand": "TeamGroup", "price": 289},
    {"name": "TeamGroup T-Force Delta RGB DDR5 64GB 6400MHz", "brand": "TeamGroup", "price": 599},



    {"name": "Corsair Vengeance LPX DDR4 16GB (2x8GB) 3200MHz", "brand": "Corsair", "price": 119},
    {"name": "Corsair Vengeance RGB Pro DDR4 32GB (2x16GB) 3600MHz", "brand": "Corsair", "price": 189},
    {"name": "Corsair Dominator Platinum DDR4 32GB 3200MHz", "brand": "Corsair", "price": 239},

    {"name": "G.Skill Ripjaws V DDR4 16GB (2x8GB) 3200MHz", "brand": "G.Skill", "price": 109},
    {"name": "G.Skill Trident Z RGB DDR4 32GB (2x16GB) 3600MHz", "brand": "G.Skill", "price": 199},
    {"name": "G.Skill Aegis DDR4 8GB 3000MHz", "brand": "G.Skill", "price": 49},

    {"name": "Kingston HyperX Fury DDR4 16GB (2x8GB) 3200MHz", "brand": "Kingston", "price": 115},
    {"name": "Kingston FURY Beast RGB DDR4 32GB (2x16GB) 3600MHz", "brand": "Kingston", "price": 185},
    {"name": "Kingston HyperX Predator DDR4 64GB 3600MHz", "brand": "Kingston", "price": 369},

    {"name": "Crucial Ballistix DDR4 16GB (2x8GB) 3200MHz", "brand": "Crucial", "price": 105},
    {"name": "Crucial DDR4 8GB 2666MHz", "brand": "Crucial", "price": 42},
    {"name": "Crucial Ballistix RGB DDR4 32GB 3600MHz", "brand": "Crucial", "price": 175},

    {"name": "TeamGroup T-Force Vulcan Z DDR4 16GB (2x8GB) 3200MHz", "brand": "TeamGroup", "price": 99},
    {"name": "TeamGroup T-Force Delta RGB DDR4 32GB 3600MHz", "brand": "TeamGroup", "price": 169},
    {"name": "TeamGroup Elite DDR4 8GB 2666MHz", "brand": "TeamGroup", "price": 39},
]
for RAM in RAMs:
    Product.objects.get_or_create(
        name=RAM["name"],
        part=RAM_part,
        brand=RAM["brand"],
        price=RAM["price"]
    )


ram_specs = [
    # DDR5 RAM
    {"name": "Corsair Vengeance DDR5 32GB (2x16GB) 6000MHz CL36", "GEN": "DDR5", "Speed": 6000, "Modules_Num": 2, "Capacity": 32},
    {"name": "Corsair Dominator Platinum RGB DDR5 32GB 6400MHz", "GEN": "DDR5", "Speed": 6400, "Modules_Num": 1, "Capacity": 32},
    {"name": "Corsair Vengeance DDR5 16GB (1x16GB) 5600MHz", "GEN": "DDR5", "Speed": 5600, "Modules_Num": 1, "Capacity": 16},
    {"name": "G.Skill Trident Z5 RGB DDR5 32GB (2x16GB) 6000MHz", "GEN": "DDR5", "Speed": 6000, "Modules_Num": 2, "Capacity": 32},
    {"name": "G.Skill Ripjaws S5 DDR5 32GB 5600MHz CL36", "GEN": "DDR5", "Speed": 5600, "Modules_Num": 1, "Capacity": 32},
    {"name": "G.Skill Trident Z5 RGB DDR5 64GB (2x32GB) 6400MHz", "GEN": "DDR5", "Speed": 6400, "Modules_Num": 2, "Capacity": 64},
    {"name": "Kingston FURY Beast DDR5 32GB (2x16GB) 6000MT/s", "GEN": "DDR5", "Speed": 6000, "Modules_Num": 2, "Capacity": 32},
    {"name": "Kingston FURY Beast RGB DDR5 16GB 5600MT/s", "GEN": "DDR5", "Speed": 5600, "Modules_Num": 1, "Capacity": 16},
    {"name": "Kingston FURY Renegade DDR5 32GB 6400MT/s", "GEN": "DDR5", "Speed": 6400, "Modules_Num": 1, "Capacity": 32},
    {"name": "Crucial DDR5 32GB (2x16GB) 5600MT/s", "GEN": "DDR5", "Speed": 5600, "Modules_Num": 2, "Capacity": 32},
    {"name": "Crucial DDR5 16GB 5200MT/s", "GEN": "DDR5", "Speed": 5200, "Modules_Num": 1, "Capacity": 16},
    {"name": "TeamGroup T-Force Delta RGB DDR5 32GB 6000MHz", "GEN": "DDR5", "Speed": 6000, "Modules_Num": 1, "Capacity": 32},
    {"name": "TeamGroup T-Force Vulcan DDR5 32GB 5600MHz", "GEN": "DDR5", "Speed": 5600, "Modules_Num": 1, "Capacity": 32},
    {"name": "TeamGroup T-Force Delta RGB DDR5 64GB 6400MHz", "GEN": "DDR5", "Speed": 6400, "Modules_Num": 1, "Capacity": 64},

    # DDR4 RAM
    {"name": "Corsair Vengeance LPX DDR4 16GB (2x8GB) 3200MHz", "GEN": "DDR4", "Speed": 3200, "Modules_Num": 2, "Capacity": 16},
    {"name": "Corsair Vengeance RGB Pro DDR4 32GB (2x16GB) 3600MHz", "GEN": "DDR4", "Speed": 3600, "Modules_Num": 2, "Capacity": 32},
    {"name": "Corsair Dominator Platinum DDR4 32GB 3200MHz", "GEN": "DDR4", "Speed": 3200, "Modules_Num": 1, "Capacity": 32},
    {"name": "G.Skill Ripjaws V DDR4 16GB (2x8GB) 3200MHz", "GEN": "DDR4", "Speed": 3200, "Modules_Num": 2, "Capacity": 16},
    {"name": "G.Skill Trident Z RGB DDR4 32GB (2x16GB) 3600MHz", "GEN": "DDR4", "Speed": 3600, "Modules_Num": 2, "Capacity": 32},
    {"name": "G.Skill Aegis DDR4 8GB 3000MHz", "GEN": "DDR4", "Speed": 3000, "Modules_Num": 1, "Capacity": 8},
    {"name": "Kingston HyperX Fury DDR4 16GB (2x8GB) 3200MHz", "GEN": "DDR4", "Speed": 3200, "Modules_Num": 2, "Capacity": 16},
    {"name": "Kingston FURY Beast RGB DDR4 32GB (2x16GB) 3600MHz", "GEN": "DDR4", "Speed": 3600, "Modules_Num": 2, "Capacity": 32},
    {"name": "Kingston HyperX Predator DDR4 64GB 3600MHz", "GEN": "DDR4", "Speed": 3600, "Modules_Num": 1, "Capacity": 64},
    {"name": "Crucial Ballistix DDR4 16GB (2x8GB) 3200MHz", "GEN": "DDR4", "Speed": 3200, "Modules_Num": 2, "Capacity": 16},
    {"name": "Crucial DDR4 8GB 2666MHz", "GEN": "DDR4", "Speed": 2666, "Modules_Num": 1, "Capacity": 8},
    {"name": "Crucial Ballistix RGB DDR4 32GB 3600MHz", "GEN": "DDR4", "Speed": 3600, "Modules_Num": 1, "Capacity": 32},
    {"name": "TeamGroup T-Force Vulcan Z DDR4 16GB (2x8GB) 3200MHz", "GEN": "DDR4", "Speed": 3200, "Modules_Num": 2, "Capacity": 16},
    {"name": "TeamGroup T-Force Delta RGB DDR4 32GB 3600MHz", "GEN": "DDR4", "Speed": 3600, "Modules_Num": 1, "Capacity": 32},
    {"name": "TeamGroup Elite DDR4 8GB 2666MHz", "GEN": "DDR4", "Speed": 2666, "Modules_Num": 1, "Capacity": 8}
]

PartSpec.objects.get_or_create(name="GEN",part=RAM_part)
PartSpec.objects.get_or_create(name="Speed",part=RAM_part)
PartSpec.objects.get_or_create(name="Modules_Num",part=RAM_part)
PartSpec.objects.get_or_create(name="Capacity",part=RAM_part)


GEN=PartSpec.objects.get(name="GEN",part=RAM_part)
Speed=PartSpec.objects.get(name="Speed",part=RAM_part)
Modules_Num=PartSpec.objects.get(name="Modules_Num",part=RAM_part)
Capacity=PartSpec.objects.get(name="Capacity",part=RAM_part)


for product in ram_specs:
    THEproduct=Product.objects.get(name=product["name"])
    ProductSpec.objects.get_or_create(product=THEproduct,part_spec=GEN,value=product["GEN"])
    ProductSpec.objects.get_or_create(product=THEproduct, part_spec=Speed, value=product["Speed"])
    ProductSpec.objects.get_or_create(product=THEproduct, part_spec=Modules_Num, value=product["Modules_Num"])
    ProductSpec.objects.get_or_create(product=THEproduct, part_spec=Capacity, value=product["Capacity"])





