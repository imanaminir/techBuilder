from pcBuilder.models import Product, Part

cpu_part, _ = Part.objects.get_or_create(name='CPU')

cpus = [
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
    {"name": "Intel Core i5-12400F", "brand": "Intel", "price": 179},
    {"name": "Intel Core i5-11400", "brand": "Intel", "price": 169},
    {"name": "Intel Core i5-10400", "brand": "Intel", "price": 159},

    # Intel Core i3 Series
    {"name": "Intel Core i3-13100", "brand": "Intel", "price": 149},
    {"name": "Intel Core i3-12100", "brand": "Intel", "price": 129},
    {"name": "Intel Core i3-10100", "brand": "Intel", "price": 119},

    # AMD Ryzen 9
    {"name": "AMD Ryzen 9 7950X", "brand": "AMD", "price": 699},
    {"name": "AMD Ryzen 9 7900X", "brand": "AMD", "price": 549},
    {"name": "AMD Ryzen 9 5900X", "brand": "AMD", "price": 549},
    {"name": "AMD Ryzen 9 3950X", "brand": "AMD", "price": 749},

    # AMD Ryzen 7
    {"name": "AMD Ryzen 7 7800X3D", "brand": "AMD", "price": 449},
    {"name": "AMD Ryzen 7 7700X", "brand": "AMD", "price": 399},
    {"name": "AMD Ryzen 7 5800X", "brand": "AMD", "price": 399},
    {"name": "AMD Ryzen 7 5700X", "brand": "AMD", "price": 329},
    {"name": "AMD Ryzen 7 3800X", "brand": "AMD", "price": 359},

    # AMD Ryzen 5
    {"name": "AMD Ryzen 5 7600X", "brand": "AMD", "price": 299},
    {"name": "AMD Ryzen 5 5600X", "brand": "AMD", "price": 299},
    {"name": "AMD Ryzen 5 5600", "brand": "AMD", "price": 199},
    {"name": "AMD Ryzen 5 3600", "brand": "AMD", "price": 189},
    {"name": "AMD Ryzen 5 2600", "brand": "AMD", "price": 149},

    # AMD Ryzen 3
    {"name": "AMD Ryzen 3 4100", "brand": "AMD", "price": 99},
    {"name": "AMD Ryzen 3 3200G", "brand": "AMD", "price": 79},

]

for cpu in cpus:
    Product.objects.get_or_create(
        name=cpu["name"],
        part=cpu_part,
        brand=cpu["brand"],
        price=cpu["price"]
    )
