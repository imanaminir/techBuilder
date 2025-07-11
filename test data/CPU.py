import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'techBuilder.settings')
django.setup()

from pcBuilder.models import Product, Part
Part.objects.get(name="CPU")
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
    Product.objects.create(
        name=CPU["name"],
        part=CPU_part,
        brand=CPU["brand"],
        price=CPU["price"]
    )


CPUS_spec=[
        # Intel Core i9 (LGA 1700 for 12th-14th Gen, LGA 1200 for 10th-11th Gen)
        {"name": "Intel Core i9-14900K", "Generation": "Intel 14", "RAM Generations Supported": ["DDR4", "DDR5"],
         "TDP (Watts)": 253, "Multicore Score": 38000, "Socket": "LGA 1700"},
        {"name": "Intel Core i9-13900K", "Generation": "Intel 13", "RAM Generations Supported": ["DDR4", "DDR5"],
         "TDP (Watts)": 253, "Multicore Score": 36000, "Socket": "LGA 1700"},
        {"name": "Intel Core i9-12900K", "Generation": "Intel 12", "RAM Generations Supported": ["DDR4", "DDR5"],
         "TDP (Watts)": 241, "Multicore Score": 27000, "Socket": "LGA 1700"},
        {"name": "Intel Core i9-11900K", "Generation": "Intel 11", "RAM Generations Supported": ["DDR4"],
         "TDP (Watts)": 250, "Multicore Score": 15000, "Socket": "LGA 1200"},
        {"name": "Intel Core i9-10900K", "Generation": "Intel 10", "RAM Generations Supported": ["DDR4"],
         "TDP (Watts)": 250, "Multicore Score": 14000, "Socket": "LGA 1200"},

        # Intel Core i7
        {"name": "Intel Core i7-14700K", "Generation": "Intel 14", "RAM Generations Supported": ["DDR4", "DDR5"],
         "TDP (Watts)": 253, "Multicore Score": 30000, "Socket": "LGA 1700"},
        {"name": "Intel Core i7-13700K", "Generation": "Intel 13", "RAM Generations Supported": ["DDR4", "DDR5"],
         "TDP (Watts)": 253, "Multicore Score": 28000, "Socket": "LGA 1700"},
        {"name": "Intel Core i7-12700K", "Generation": "Intel 12", "RAM Generations Supported": ["DDR4", "DDR5"],
         "TDP (Watts)": 190, "Multicore Score": 23000, "Socket": "LGA 1700"},
        {"name": "Intel Core i7-11700K", "Generation": "Intel 11", "RAM Generations Supported": ["DDR4"],
         "TDP (Watts)": 250, "Multicore Score": 14000, "Socket": "LGA 1200"},
        {"name": "Intel Core i7-10700K", "Generation": "Intel 10", "RAM Generations Supported": ["DDR4"],
         "TDP (Watts)": 229, "Multicore Score": 12000, "Socket": "LGA 1200"},

        # Intel Core i5
        {"name": "Intel Core i5-14600K", "Generation": "Intel 14", "RAM Generations Supported": ["DDR4", "DDR5"],
         "TDP (Watts)": 181, "Multicore Score": 24000, "Socket": "LGA 1700"},
        {"name": "Intel Core i5-13600K", "Generation": "Intel 13", "RAM Generations Supported": ["DDR4", "DDR5"],
         "TDP (Watts)": 181, "Multicore Score": 22000, "Socket": "LGA 1700"},
        {"name": "Intel Core i5-12600K", "Generation": "Intel 12", "RAM Generations Supported": ["DDR4", "DDR5"],
         "TDP (Watts)": 150, "Multicore Score": 17000, "Socket": "LGA 1700"},
        {"name": "Intel Core i5-11600K", "Generation": "Intel 11", "RAM Generations Supported": ["DDR4"],
         "TDP (Watts)": 182, "Multicore Score": 11000, "Socket": "LGA 1200"},
        {"name": "Intel Core i5-10600K", "Generation": "Intel 10", "RAM Generations Supported": ["DDR4"],
         "TDP (Watts)": 182, "Multicore Score": 9500, "Socket": "LGA 1200"},

        # Intel Core i3
        {"name": "Intel Core i3-13100", "Generation": "Intel 13", "RAM Generations Supported": ["DDR4", "DDR5"],
         "TDP (Watts)": 60, "Multicore Score": 8000, "Socket": "LGA 1700"},
        {"name": "Intel Core i3-12100", "Generation": "Intel 12", "RAM Generations Supported": ["DDR4", "DDR5"],
         "TDP (Watts)": 60, "Multicore Score": 7500, "Socket": "LGA 1700"},
        {"name": "Intel Core i3-10100", "Generation": "Intel 10", "RAM Generations Supported": ["DDR4"],
         "TDP (Watts)": 65, "Multicore Score": 5500, "Socket": "LGA 1200"},

        # AMD Ryzen 9 (AM5 for Ryzen 7000, AM4 for Ryzen 3000/5000)
        {"name": "AMD Ryzen 9 7950X", "Generation": "AMD 5", "RAM Generations Supported": ["DDR5"], "TDP (Watts)": 230,
         "Multicore Score": 38000, "Socket": "AM5"},
        {"name": "AMD Ryzen 9 5900X", "Generation": "AMD 4", "RAM Generations Supported": ["DDR4"], "TDP (Watts)": 142,
         "Multicore Score": 21000, "Socket": "AM4"},
        {"name": "AMD Ryzen 9 3950X", "Generation": "AMD 3", "RAM Generations Supported": ["DDR4"], "TDP (Watts)": 142,
         "Multicore Score": 18000, "Socket": "AM4"},

        # AMD Ryzen 7
        {"name": "AMD Ryzen 7 7800X3D", "Generation": "AMD 5", "RAM Generations Supported": ["DDR5"],
         "TDP (Watts)": 120, "Multicore Score": 19000, "Socket": "AM5"},
        {"name": "AMD Ryzen 7 5800X", "Generation": "AMD 4", "RAM Generations Supported": ["DDR4"], "TDP (Watts)": 142,
         "Multicore Score": 15000, "Socket": "AM4"},
        {"name": "AMD Ryzen 7 3800X", "Generation": "AMD 3", "RAM Generations Supported": ["DDR4"], "TDP (Watts)": 142,
         "Multicore Score": 12500, "Socket": "AM4"},

        # AMD Ryzen 5
        {"name": "AMD Ryzen 5 7600X", "Generation": "AMD 5", "RAM Generations Supported": ["DDR5"], "TDP (Watts)": 105,
         "Multicore Score": 15000, "Socket": "AM5"},
        {"name": "AMD Ryzen 5 5600", "Generation": "AMD 4", "RAM Generations Supported": ["DDR4"], "TDP (Watts)": 88,
         "Multicore Score": 11000, "Socket": "AM4"},
        {"name": "AMD Ryzen 5 3600", "Generation": "AMD 3", "RAM Generations Supported": ["DDR4"], "TDP (Watts)": 88,
         "Multicore Score": 9000, "Socket": "AM4"}

]