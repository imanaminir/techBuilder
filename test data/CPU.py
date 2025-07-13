import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'techBuilder.settings')
django.setup()

from pcBuilder.models import Product, Part , PartSpec,ProductSpec
Part.objects.get_or_create(name="CPU")
CPU_part = Part.objects.get(name="CPU")

CPUs = [
    # Intel Core i9 Series
    {"name": "Intel Core i9-14900K", "brand": "Intel", "price": 589},
    {"name": "Intel Core i9-13900K", "brand": "Intel", "price": 569},
    {"name": "Intel Core i9-12900K", "brand": "Intel", "price": 499},
    {"name": "Intel Core i9-11900K", "brand": "Intel", "price": 439},
    {"name": "Intel Core i9-10900K", "brand": "Intel", "price": 429},

    # Intel Core i7 Series
    {"name": "Intel Core i7-14700K", "brand": "Intel", "price": 409},
    {"name": "Intel Core i7-13700K", "brand": "Intel", "price": 389},
    {"name": "Intel Core i7-12700K", "brand": "Intel", "price": 379},
    {"name": "Intel Core i7-11700K", "brand": "Intel", "price": 359},
    {"name": "Intel Core i7-10700K", "brand": "Intel", "price": 349},

    # Intel Core i5 Series
    {"name": "Intel Core i5-14600K", "brand": "Intel", "price": 319},
    {"name": "Intel Core i5-13600K", "brand": "Intel", "price": 299},
    {"name": "Intel Core i5-12600K", "brand": "Intel", "price": 279},
    {"name": "Intel Core i5-11600K", "brand": "Intel", "price": 249},
    {"name": "Intel Core i5-10600K", "brand": "Intel", "price": 229},

    # Intel Core i3 Series
    {"name": "Intel Core i3-13100", "brand": "Intel", "price": 149},
    {"name": "Intel Core i3-12100", "brand": "Intel", "price": 129},
    {"name": "Intel Core i3-10100", "brand": "Intel", "price": 119},

    # AMD Ryzen 9
    {"name": "AMD Ryzen 9 7950X", "brand": "AMD", "price": 699},
    {"name": "AMD Ryzen 9 5900X", "brand": "AMD", "price": 549},
    {"name": "AMD Ryzen 9 3950X", "brand": "AMD", "price": 749},

    # AMD Ryzen 7
    {"name": "AMD Ryzen 7 7800X3D", "brand": "AMD", "price": 449},
    {"name": "AMD Ryzen 7 5800X", "brand": "AMD", "price": 399},
    {"name": "AMD Ryzen 7 3800X", "brand": "AMD", "price": 359},

    # AMD Ryzen 5
    {"name": "AMD Ryzen 5 7600X", "brand": "AMD", "price": 299},
    {"name": "AMD Ryzen 5 5600", "brand": "AMD", "price": 199},
    {"name": "AMD Ryzen 5 3600", "brand": "AMD", "price": 189},

]
for CPU in CPUs:
    Product.objects.get_or_create(
        name=CPU["name"],
        part=CPU_part,
        brand=CPU["brand"],
        price=CPU["price"]
    )


CPUS_spec=[
        # Intel Core i9 (LGA 1700 for 12th-14th Gen, LGA 1200 for 10th-11th Gen)
        {"name": "Intel Core i9-14900K", "GEN": "Intel 14", "RAM_GENs": ["DDR4", "DDR5"],
         "TDP": 253, "Multicore": 38000, "Socket": "LGA 1700"},
        {"name": "Intel Core i9-13900K", "GEN": "Intel 13", "RAM_GENs": ["DDR4", "DDR5"],
         "TDP": 253, "Multicore": 36000, "Socket": "LGA 1700"},
        {"name": "Intel Core i9-12900K", "GEN": "Intel 12", "RAM_GENs": ["DDR4", "DDR5"],
         "TDP": 241, "Multicore": 27000, "Socket": "LGA 1700"},
        {"name": "Intel Core i9-11900K", "GEN": "Intel 11", "RAM_GENs": ["DDR4"],
         "TDP": 250, "Multicore": 15000, "Socket": "LGA 1200"},
        {"name": "Intel Core i9-10900K", "GEN": "Intel 10", "RAM_GENs": ["DDR4"],
         "TDP": 250, "Multicore": 14000, "Socket": "LGA 1200"},

        # Intel Core i7
        {"name": "Intel Core i7-14700K", "GEN": "Intel 14", "RAM_GENs": ["DDR4", "DDR5"],
         "TDP": 253, "Multicore": 30000, "Socket": "LGA 1700"},
        {"name": "Intel Core i7-13700K", "GEN": "Intel 13", "RAM_GENs": ["DDR4", "DDR5"],
         "TDP": 253, "Multicore": 28000, "Socket": "LGA 1700"},
        {"name": "Intel Core i7-12700K", "GEN": "Intel 12", "RAM_GENs": ["DDR4", "DDR5"],
         "TDP": 190, "Multicore": 23000, "Socket": "LGA 1700"},
        {"name": "Intel Core i7-11700K", "GEN": "Intel 11", "RAM_GENs": ["DDR4"],
         "TDP": 250, "Multicore": 14000, "Socket": "LGA 1200"},
        {"name": "Intel Core i7-10700K", "GEN": "Intel 10", "RAM_GENs": ["DDR4"],
         "TDP": 229, "Multicore": 12000, "Socket": "LGA 1200"},

        # Intel Core i5
        {"name": "Intel Core i5-14600K", "GEN": "Intel 14", "RAM_GENs": ["DDR4", "DDR5"],
         "TDP": 181, "Multicore": 24000, "Socket": "LGA 1700"},
        {"name": "Intel Core i5-13600K", "GEN": "Intel 13", "RAM_GENs": ["DDR4", "DDR5"],
         "TDP": 181, "Multicore": 22000, "Socket": "LGA 1700"},
        {"name": "Intel Core i5-12600K", "GEN": "Intel 12", "RAM_GENs": ["DDR4", "DDR5"],
         "TDP": 150, "Multicore": 17000, "Socket": "LGA 1700"},
        {"name": "Intel Core i5-11600K", "GEN": "Intel 11", "RAM_GENs": ["DDR4"],
         "TDP": 182, "Multicore": 11000, "Socket": "LGA 1200"},
        {"name": "Intel Core i5-10600K", "GEN": "Intel 10", "RAM_GENs": ["DDR4"],
         "TDP": 182, "Multicore": 9500, "Socket": "LGA 1200"},

        # Intel Core i3
        {"name": "Intel Core i3-13100", "GEN": "Intel 13", "RAM_GENs": ["DDR4", "DDR5"],
         "TDP": 60, "Multicore": 8000, "Socket": "LGA 1700"},
        {"name": "Intel Core i3-12100", "GEN": "Intel 12", "RAM_GENs": ["DDR4", "DDR5"],
         "TDP": 60, "Multicore": 7500, "Socket": "LGA 1700"},
        {"name": "Intel Core i3-10100", "GEN": "Intel 10", "RAM_GENs": ["DDR4"],
         "TDP": 65, "Multicore": 5500, "Socket": "LGA 1200"},

        # AMD Ryzen 9 (AM5 for Ryzen 7000, AM4 for Ryzen 3000/5000)
        {"name": "AMD Ryzen 9 7950X", "GEN": "AMD 5", "RAM_GENs": ["DDR5"], "TDP": 230,
         "Multicore": 38000, "Socket": "AM5"},
        {"name": "AMD Ryzen 9 5900X", "GEN": "AMD 4", "RAM_GENs": ["DDR4"], "TDP": 142,
         "Multicore": 21000, "Socket": "AM4"},
        {"name": "AMD Ryzen 9 3950X", "GEN": "AMD 3", "RAM_GENs": ["DDR4"], "TDP": 142,
         "Multicore": 18000, "Socket": "AM4"},

        # AMD Ryzen 7
        {"name": "AMD Ryzen 7 7800X3D", "GEN": "AMD 5", "RAM_GENs": ["DDR5"],
         "TDP": 120, "Multicore": 19000, "Socket": "AM5"},
        {"name": "AMD Ryzen 7 5800X", "GEN": "AMD 4", "RAM_GENs": ["DDR4"], "TDP": 142,
         "Multicore": 15000, "Socket": "AM4"},
        {"name": "AMD Ryzen 7 3800X", "GEN": "AMD 3", "RAM_GENs": ["DDR4"], "TDP": 142,
         "Multicore": 12500, "Socket": "AM4"},

        # AMD Ryzen 5
        {"name": "AMD Ryzen 5 7600X", "GEN": "AMD 5", "RAM_GENs": ["DDR5"], "TDP": 105,
         "Multicore": 15000, "Socket": "AM5"},
        {"name": "AMD Ryzen 5 5600", "GEN": "AMD 4", "RAM_GENs": ["DDR4"], "TDP": 88,
         "Multicore": 11000, "Socket": "AM4"},
        {"name": "AMD Ryzen 5 3600", "GEN": "AMD 3", "RAM_GENs": ["DDR4"], "TDP": 88,
         "Multicore": 9000, "Socket": "AM4"}

]
PartSpec.objects.get_or_create(name="GEN",part=CPU_part)
PartSpec.objects.get_or_create(name="RAM_GENs",part=CPU_part)
PartSpec.objects.get_or_create(name="TDP",part=CPU_part)
PartSpec.objects.get_or_create(name="Multicore",part=CPU_part)
PartSpec.objects.get_or_create(name="Socket",part=CPU_part)

GEN=PartSpec.objects.get(name="GEN",part=CPU_part)
RAM_GENs=PartSpec.objects.get(name="RAM_GENs",part=CPU_part)
TDP=PartSpec.objects.get(name="TDP",part=CPU_part)
Multicore=PartSpec.objects.get(name="Multicore",part=CPU_part)
Socket=PartSpec.objects.get(name="Socket",part=CPU_part)

for product in CPUS_spec:
    THEproduct=Product.objects.get(name=product["name"])
    ProductSpec.objects.get_or_create(product=THEproduct,part_spec=GEN,value=product["GEN"])
    ProductSpec.objects.get_or_create(product=THEproduct, part_spec=RAM_GENs, value=product["RAM_GENs"])
    ProductSpec.objects.get_or_create(product=THEproduct, part_spec=TDP, value=product["TDP"])
    ProductSpec.objects.get_or_create(product=THEproduct, part_spec=Multicore, value=product["Multicore"])
    ProductSpec.objects.get_or_create(product=THEproduct,part_spec=Socket,value=product["Socket"])


