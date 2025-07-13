import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'techBuilder.settings')
django.setup()

from pcBuilder.models import Product, Part, PartSpec,ProductSpec
Part.objects.get_or_create(name="GPU")
GPU_part = Part.objects.get(name="GPU")


GPUs =[
    {"name": "NVIDIA GeForce RTX 5090 Founders Edition", "brand": "NVIDIA", "price": 1799},
    {"name": "ASUS ROG STRIX RTX 5090 OC Edition", "brand": "ASUS", "price": 1999},
    {"name": "MSI SUPRIM X RTX 5090 24GB", "brand": "MSI", "price": 1949},
    {"name": "Gigabyte AORUS Master RTX 5090", "brand": "Gigabyte", "price": 1899},
    {"name": "ZOTAC GAMING AMP Extreme RTX 5090", "brand": "ZOTAC", "price": 1879},

    {"name": "NVIDIA GeForce RTX 5080 Founders Edition", "brand": "NVIDIA", "price": 1199},
    {"name": "ASUS TUF Gaming RTX 5080 OC", "brand": "ASUS", "price": 1249},
    {"name": "MSI Gaming X Trio RTX 5080", "brand": "MSI", "price": 1229},
    {"name": "Gigabyte Eagle RTX 5080", "brand": "Gigabyte", "price": 1179},
    {"name": "ZOTAC Twin Edge RTX 5080", "brand": "ZOTAC", "price": 1150},

    {"name": "NVIDIA GeForce RTX 5070 Founders Edition", "brand": "NVIDIA", "price": 849},
    {"name": "ASUS Dual RTX 5070 OC", "brand": "ASUS", "price": 879},
    {"name": "MSI Ventus 3X RTX 5070", "brand": "MSI", "price": 869},
    {"name": "Gigabyte Windforce RTX 5070", "brand": "Gigabyte", "price": 859},
    {"name": "ZOTAC RTX 5070 Trinity", "brand": "ZOTAC", "price": 839},

    {"name": "NVIDIA GeForce RTX 5060 Ti Founders Edition", "brand": "NVIDIA", "price": 599},
    {"name": "ASUS TUF RTX 5060 Ti", "brand": "ASUS", "price": 629},
    {"name": "MSI Ventus 2X RTX 5060 Ti", "brand": "MSI", "price": 619},
    {"name": "Gigabyte RTX 5060 Ti Gaming OC", "brand": "Gigabyte", "price": 609},
    {"name": "ZOTAC RTX 5060 Ti Twin Edge", "brand": "ZOTAC", "price": 599},

    {"name": "NVIDIA GeForce RTX 5060", "brand": "NVIDIA", "price": 449},
    {"name": "ASUS Dual RTX 5060", "brand": "ASUS", "price": 469},
    {"name": "Gigabyte Windforce RTX 5060", "brand": "Gigabyte", "price": 459},
    {"name": "ZOTAC RTX 5060", "brand": "ZOTAC", "price": 449},






    {"name": "NVIDIA GeForce RTX 4090 Founders Edition", "brand": "NVIDIA", "price": 1599},
    {"name": "ASUS ROG STRIX RTX 4090 OC", "brand": "ASUS", "price": 1799},
    {"name": "MSI Suprim X RTX 4090", "brand": "MSI", "price": 1749},
    {"name": "Gigabyte AORUS Master RTX 4090", "brand": "Gigabyte", "price": 1729},

    {"name": "NVIDIA GeForce RTX 4080 Founders Edition", "brand": "NVIDIA", "price": 1199},
    {"name": "ASUS TUF Gaming RTX 4080 OC", "brand": "ASUS", "price": 1249},
    {"name": "Gigabyte Eagle RTX 4080", "brand": "Gigabyte", "price": 1179},
    {"name": "ZOTAC GAMING Trinity RTX 4080", "brand": "ZOTAC", "price": 1149},

    {"name": "NVIDIA GeForce RTX 4070 Ti Founders Edition", "brand": "NVIDIA", "price": 849},
    {"name": "ASUS Dual RTX 4070 Ti OC", "brand": "ASUS", "price": 879},
    {"name": "MSI Ventus 3X RTX 4070 Ti", "brand": "MSI", "price": 859},
    {"name": "Gigabyte Gaming OC RTX 4070 Ti", "brand": "Gigabyte", "price": 839},

    {"name": "NVIDIA GeForce RTX 4070 Founders Edition", "brand": "NVIDIA", "price": 599},
    {"name": "ASUS TUF RTX 4070", "brand": "ASUS", "price": 629},
    {"name": "Gigabyte Windforce RTX 4070", "brand": "Gigabyte", "price": 609},
    {"name": "ZOTAC Twin Edge RTX 4070", "brand": "ZOTAC", "price": 589},

    {"name": "NVIDIA GeForce RTX 4060 Ti 16GB", "brand": "NVIDIA", "price": 449},
    {"name": "ASUS Dual RTX 4060 Ti OC", "brand": "ASUS", "price": 469},
    {"name": "MSI Gaming X RTX 4060 Ti", "brand": "MSI", "price": 459},
    {"name": "Gigabyte AERO OC RTX 4060 Ti", "brand": "Gigabyte", "price": 449},

    {"name": "NVIDIA GeForce RTX 4060", "brand": "NVIDIA", "price": 329},
    {"name": "ASUS Dual RTX 4060", "brand": "ASUS", "price": 339},
    {"name": "ZOTAC Twin Edge RTX 4060", "brand": "ZOTAC", "price": 319},
    {"name": "Gigabyte Windforce RTX 4060", "brand": "Gigabyte", "price": 309},

    {"name": "NVIDIA GeForce RTX 4050 Founders Edition", "brand": "NVIDIA", "price": 269},
    {"name": "ASUS Dual RTX 4050 OC", "brand": "ASUS", "price": 289},
    {"name": "MSI Ventus 2X RTX 4050", "brand": "MSI", "price": 279},
    {"name": "Gigabyte Windforce RTX 4050", "brand": "Gigabyte", "price": 269},
    {"name": "ZOTAC Twin Edge RTX 4050", "brand": "ZOTAC", "price": 265},





    {"name": "NVIDIA GeForce RTX 3090 Ti Founders Edition", "brand": "NVIDIA", "price": 1299},
    {"name": "ASUS ROG Strix RTX 3090 Ti OC", "brand": "ASUS", "price": 1399},
    {"name": "MSI Suprim X RTX 3090 Ti", "brand": "MSI", "price": 1349},
    {"name": "Gigabyte AORUS Master RTX 3090 Ti", "brand": "Gigabyte", "price": 1329},

    {"name": "NVIDIA GeForce RTX 3080 Ti Founders Edition", "brand": "NVIDIA", "price": 899},
    {"name": "ASUS TUF Gaming RTX 3080 Ti OC", "brand": "ASUS", "price": 949},
    {"name": "Gigabyte Eagle RTX 3080 Ti", "brand": "Gigabyte", "price": 929},
    {"name": "ZOTAC Trinity RTX 3080 Ti", "brand": "ZOTAC", "price": 899},

    {"name": "NVIDIA GeForce RTX 3080 Founders Edition", "brand": "NVIDIA", "price": 699},
    {"name": "ASUS Dual RTX 3080 OC", "brand": "ASUS", "price": 749},
    {"name": "MSI Gaming X Trio RTX 3080", "brand": "MSI", "price": 739},
    {"name": "Gigabyte Windforce RTX 3080", "brand": "Gigabyte", "price": 719},

    {"name": "NVIDIA GeForce RTX 3070 Ti Founders Edition", "brand": "NVIDIA", "price": 529},
    {"name": "ASUS Dual RTX 3070 Ti OC", "brand": "ASUS", "price": 559},
    {"name": "MSI Ventus 3X RTX 3070 Ti", "brand": "MSI", "price": 539},
    {"name": "Gigabyte Gaming OC RTX 3070 Ti", "brand": "Gigabyte", "price": 519},

    {"name": "NVIDIA GeForce RTX 3070 Founders Edition", "brand": "NVIDIA", "price": 449},
    {"name": "ASUS TUF RTX 3070", "brand": "ASUS", "price": 479},
    {"name": "Gigabyte Eagle RTX 3070", "brand": "Gigabyte", "price": 459},
    {"name": "ZOTAC Twin Edge RTX 3070", "brand": "ZOTAC", "price": 439},

    {"name": "NVIDIA GeForce RTX 3060 Ti Founders Edition", "brand": "NVIDIA", "price": 399},
    {"name": "ASUS Dual RTX 3060 Ti OC", "brand": "ASUS", "price": 429},
    {"name": "MSI Ventus 2X RTX 3060 Ti", "brand": "MSI", "price": 409},
    {"name": "Gigabyte AERO OC RTX 3060 Ti", "brand": "Gigabyte", "price": 399},

    {"name": "NVIDIA GeForce RTX 3060 Founders Edition", "brand": "NVIDIA", "price": 329},
    {"name": "ASUS Dual RTX 3060", "brand": "ASUS", "price": 359},
    {"name": "Gigabyte Windforce RTX 3060", "brand": "Gigabyte", "price": 339},
    {"name": "ZOTAC Twin Edge RTX 3060", "brand": "ZOTAC", "price": 329},

    {"name": "NVIDIA GeForce RTX 3050 Founders Edition", "brand": "NVIDIA", "price": 229},
    {"name": "ASUS Dual RTX 3050 OC", "brand": "ASUS", "price": 239},
    {"name": "MSI Ventus 2X RTX 3050", "brand": "MSI", "price": 235},
    {"name": "Gigabyte Eagle RTX 3050", "brand": "Gigabyte", "price": 229},
    {"name": "ZOTAC Twin Edge RTX 3050", "brand": "ZOTAC", "price": 219},




    {"name": "AMD Radeon RX 7900 XTX 24GB", "brand": "AMD", "price": 999},
    {"name": "Sapphire Nitro+ RX 7900 XTX", "brand": "Sapphire", "price": 1049},
    {"name": "ASUS TUF Gaming RX 7900 XTX OC", "brand": "ASUS", "price": 1079},
    {"name": "PowerColor Red Devil RX 7900 XTX", "brand": "PowerColor", "price": 1029},

    {"name": "AMD Radeon RX 7900 XT 20GB", "brand": "AMD", "price": 799},
    {"name": "XFX Speedster MERC310 RX 7900 XT", "brand": "XFX", "price": 839},
    {"name": "ASUS TUF Gaming RX 7900 XT", "brand": "ASUS", "price": 819},
    {"name": "Sapphire Pulse RX 7900 XT", "brand": "Sapphire", "price": 799},

    {"name": "AMD Radeon RX 7800 XT 16GB", "brand": "AMD", "price": 499},
    {"name": "Sapphire Nitro+ RX 7800 XT", "brand": "Sapphire", "price": 539},
    {"name": "PowerColor Hellhound RX 7800 XT", "brand": "PowerColor", "price": 519},
    {"name": "XFX QICK319 RX 7800 XT", "brand": "XFX", "price": 509},

    {"name": "AMD Radeon RX 7700 XT 12GB", "brand": "AMD", "price": 449},
    {"name": "ASRock Phantom Gaming RX 7700 XT", "brand": "ASRock", "price": 439},
    {"name": "Sapphire Pulse RX 7700 XT", "brand": "Sapphire", "price": 429},
    {"name": "PowerColor Red Devil RX 7700 XT", "brand": "PowerColor", "price": 459},

    {"name": "AMD Radeon RX 7600 XT 16GB", "brand": "AMD", "price": 329},
    {"name": "Sapphire Pulse RX 7600 XT", "brand": "Sapphire", "price": 339},
    {"name": "XFX Speedster SWFT210 RX 7600 XT", "brand": "XFX", "price": 319},
    {"name": "PowerColor Fighter RX 7600 XT", "brand": "PowerColor", "price": 309},

    {"name": "AMD Radeon RX 7600 8GB", "brand": "AMD", "price": 269},
    {"name": "ASRock Challenger RX 7600", "brand": "ASRock", "price": 259},
    {"name": "XFX Speedster SWFT210 RX 7600", "brand": "XFX", "price": 249},
    {"name": "PowerColor Fighter RX 7600", "brand": "PowerColor", "price": 255},
    {"name": "Sapphire Pulse RX 7600", "brand": "Sapphire", "price": 265},
    {"name": "Gigabyte Gaming OC RX 7600", "brand": "Gigabyte", "price": 269},
    {"name": "MSI Mech 2X RX 7600", "brand": "MSI", "price": 259},




    {"name": "AMD Radeon RX 6950 XT 16GB", "brand": "AMD", "price": 679},
    {"name": "ASUS ROG Strix RX 6950 XT OC", "brand": "ASUS", "price": 729},
    {"name": "MSI Gaming X Trio RX 6950 XT", "brand": "MSI", "price": 699},

    {"name": "AMD Radeon RX 6900 XT 16GB", "brand": "AMD", "price": 579},
    {"name": "PowerColor Red Devil RX 6900 XT", "brand": "PowerColor", "price": 599},
    {"name": "XFX MERC319 RX 6900 XT", "brand": "XFX", "price": 589},


    {"name": "AMD Radeon RX 6800 XT 16GB", "brand": "AMD", "price": 469},
    {"name": "Sapphire Nitro+ RX 6800 XT", "brand": "Sapphire", "price": 489},
    {"name": "Gigabyte Gaming OC RX 6800 XT", "brand": "Gigabyte", "price": 479},

    {"name": "AMD Radeon RX 6750 XT 12GB", "brand": "AMD", "price": 419},
    {"name": "ASUS Dual RX 6750 XT", "brand": "ASUS", "price": 439},
    {"name": "PowerColor Hellhound RX 6750 XT", "brand": "PowerColor", "price": 429},

    {"name": "AMD Radeon RX 6700 XT 12GB", "brand": "AMD", "price": 359},
    {"name": "Sapphire Pulse RX 6700 XT", "brand": "Sapphire", "price": 369},
    {"name": "XFX Speedster QICK RX 6700 XT", "brand": "XFX", "price": 349},

    {"name": "AMD Radeon RX 6650 XT 8GB", "brand": "AMD", "price": 279},
    {"name": "MSI Mech 2X RX 6650 XT", "brand": "MSI", "price": 289},
    {"name": "Sapphire Pulse RX 6650 XT", "brand": "Sapphire", "price": 275},

    {"name": "AMD Radeon RX 6600 XT 8GB", "brand": "AMD", "price": 249},
    {"name": "ASRock Phantom Gaming RX 6600 XT", "brand": "ASRock", "price": 239},
    {"name": "XFX SWFT 210 RX 6600 XT", "brand": "XFX", "price": 229},

    {"name": "AMD Radeon RX 6600 8GB", "brand": "AMD", "price": 209},
    {"name": "PowerColor Fighter RX 6600", "brand": "PowerColor", "price": 199},
    {"name": "Sapphire Pulse RX 6600", "brand": "Sapphire", "price": 205},


    {"name": "AMD Radeon RX 6500 XT 4GB", "brand": "AMD", "price": 149},
    {"name": "ASUS Dual RX 6500 XT", "brand": "ASUS", "price": 159},
    {"name": "Sapphire Pulse RX 6500 XT", "brand": "Sapphire", "price": 145},

    {"name": "AMD Radeon RX 6400 4GB", "brand": "AMD", "price": 129},
    {"name": "ASRock Challenger RX 6400", "brand": "ASRock", "price": 119},
    {"name": "PowerColor RX 6400 ITX", "brand": "PowerColor", "price": 125}



]
for GPU in GPUs:
    Product.objects.get_or_create(
        name=GPU["name"],
        part=GPU_part,
        brand=GPU["brand"],
        price=GPU["price"]
    )

gpu_specs = [
    # RTX 50 Series (Projected Specifications)
    {"name": "NVIDIA GeForce RTX 5090 Founders Edition", "PCIe_Gen": "PCIe 5.0", "Power_Needed": 500,
     "power_connector": ["16-pin (12VHPWR)"], "PassMark_G3D": 45000},
    {"name": "ASUS ROG STRIX RTX 5090 OC Edition", "PCIe_Gen": "PCIe 5.0", "Power_Needed": 520,
     "power_connector": ["16-pin (12VHPWR)"], "PassMark_G3D": 46000},
    {"name": "MSI SUPRIM X RTX 5090 24GB", "PCIe_Gen": "PCIe 5.0", "Power_Needed": 520,
     "power_connector": ["16-pin (12VHPWR)"], "PassMark_G3D": 45800},
    {"name": "Gigabyte AORUS Master RTX 5090", "PCIe_Gen": "PCIe 5.0", "Power_Needed": 520,
     "power_connector": ["16-pin (12VHPWR)"], "PassMark_G3D": 45500},
    {"name": "ZOTAC GAMING AMP Extreme RTX 5090", "PCIe_Gen": "PCIe 5.0", "Power_Needed": 520,
     "power_connector": ["16-pin (12VHPWR)"], "PassMark_G3D": 45200},

    {"name": "NVIDIA GeForce RTX 5080 Founders Edition", "PCIe_Gen": "PCIe 5.0", "Power_Needed": 350,
     "power_connector": ["16-pin (12VHPWR)"], "PassMark_G3D": 38000},
    {"name": "ASUS TUF Gaming RTX 5080 OC", "PCIe_Gen": "PCIe 5.0", "Power_Needed": 370,
     "power_connector": ["16-pin (12VHPWR)"], "PassMark_G3D": 38500},
    {"name": "MSI Gaming X Trio RTX 5080", "PCIe_Gen": "PCIe 5.0", "Power_Needed": 370,
     "power_connector": ["16-pin (12VHPWR)"], "PassMark_G3D": 38400},
    {"name": "Gigabyte Eagle RTX 5080", "PCIe_Gen": "PCIe 5.0", "Power_Needed": 350,
     "power_connector": ["16-pin (12VHPWR)"], "PassMark_G3D": 38000},
    {"name": "ZOTAC Twin Edge RTX 5080", "PCIe_Gen": "PCIe 5.0", "Power_Needed": 350,
     "power_connector": ["16-pin (12VHPWR)"], "PassMark_G3D": 37800},

    {"name": "NVIDIA GeForce RTX 5070 Founders Edition", "PCIe_Gen": "PCIe 5.0", "Power_Needed": 250,
     "power_connector": ["8-pin", "8-pin"], "PassMark_G3D": 32000},
    {"name": "ASUS Dual RTX 5070 OC", "PCIe_Gen": "PCIe 5.0", "Power_Needed": 270,
     "power_connector": ["8-pin", "8-pin"], "PassMark_G3D": 32500},
    {"name": "MSI Ventus 3X RTX 5070", "PCIe_Gen": "PCIe 5.0", "Power_Needed": 260,
     "power_connector": ["8-pin", "8-pin"], "PassMark_G3D": 32200},
    {"name": "Gigabyte Windforce RTX 5070", "PCIe_Gen": "PCIe 5.0", "Power_Needed": 250,
     "power_connector": ["8-pin", "8-pin"], "PassMark_G3D": 32000},
    {"name": "ZOTAC RTX 5070 Trinity", "PCIe_Gen": "PCIe 5.0", "Power_Needed": 250,
     "power_connector": ["8-pin", "8-pin"], "PassMark_G3D": 31800},

    {"name": "NVIDIA GeForce RTX 5060 Ti Founders Edition", "PCIe_Gen": "PCIe 5.0", "Power_Needed": 200,
     "power_connector": ["8-pin"], "PassMark_G3D": 28000},
    {"name": "ASUS TUF RTX 5060 Ti", "PCIe_Gen": "PCIe 5.0", "Power_Needed": 220, "power_connector": ["8-pin"], "PassMark_G3D": 28500},
    {"name": "MSI Ventus 2X RTX 5060 Ti", "PCIe_Gen": "PCIe 5.0", "Power_Needed": 210,
     "power_connector": ["8-pin"], "PassMark_G3D": 28200},
    {"name": "Gigabyte RTX 5060 Ti Gaming OC", "PCIe_Gen": "PCIe 5.0", "Power_Needed": 220,
     "power_connector": ["8-pin"], "PassMark_G3D": 28400},
    {"name": "ZOTAC RTX 5060 Ti Twin Edge", "PCIe_Gen": "PCIe 5.0", "Power_Needed": 200,
     "power_connector": ["8-pin"], "PassMark_G3D": 28000},

    {"name": "NVIDIA GeForce RTX 5060", "PCIe_Gen": "PCIe 5.0", "Power_Needed": 150,
     "power_connector": ["8-pin"], "PassMark_G3D": 24000},
    {"name": "ASUS Dual RTX 5060", "PCIe_Gen": "PCIe 5.0", "Power_Needed": 160, "power_connector": ["8-pin"], "PassMark_G3D": 24500},
    {"name": "Gigabyte Windforce RTX 5060", "PCIe_Gen": "PCIe 5.0", "Power_Needed": 150,
     "power_connector": ["8-pin"], "PassMark_G3D": 24000},
    {"name": "ZOTAC RTX 5060", "PCIe_Gen": "PCIe 5.0", "Power_Needed": 150, "power_connector": ["8-pin"], "PassMark_G3D": 23800},

    # RTX 40 Series (Actual Benchmarks)
    {"name": "NVIDIA GeForce RTX 4090 Founders Edition", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 450,
     "power_connector": ["16-pin (12VHPWR)"], "PassMark_G3D": 42000},
    {"name": "ASUS ROG STRIX RTX 4090 OC", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 480,
     "power_connector": ["16-pin (12VHPWR)"], "PassMark_G3D": 42500},
    {"name": "MSI Suprim X RTX 4090", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 480,
     "power_connector": ["16-pin (12VHPWR)"], "PassMark_G3D": 42400},
    {"name": "Gigabyte AORUS Master RTX 4090", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 480,
     "power_connector": ["16-pin (12VHPWR)"], "PassMark_G3D": 42300},

    {"name": "NVIDIA GeForce RTX 4080 Founders Edition", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 320,
     "power_connector": ["16-pin (12VHPWR)"], "PassMark_G3D": 35000},
    {"name": "ASUS TUF Gaming RTX 4080 OC", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 340,
     "power_connector": ["16-pin (12VHPWR)"], "PassMark_G3D": 35500},
    {"name": "Gigabyte Eagle RTX 4080", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 320,
     "power_connector": ["16-pin (12VHPWR)"], "PassMark_G3D": 35000},
    {"name": "ZOTAC GAMING Trinity RTX 4080", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 320,
     "power_connector": ["16-pin (12VHPWR)"], "PassMark_G3D": 34800},

    {"name": "NVIDIA GeForce RTX 4070 Ti Founders Edition", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 285,
     "power_connector": ["16-pin (12VHPWR)"], "PassMark_G3D": 30000},
    {"name": "ASUS Dual RTX 4070 Ti OC", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 300,
     "power_connector": ["16-pin (12VHPWR)"], "PassMark_G3D": 30500},
    {"name": "MSI Ventus 3X RTX 4070 Ti", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 290,
     "power_connector": ["16-pin (12VHPWR)"], "PassMark_G3D": 30200},
    {"name": "Gigabyte Gaming OC RTX 4070 Ti", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 300,
     "power_connector": ["16-pin (12VHPWR)"], "PassMark_G3D": 30400},

    {"name": "NVIDIA GeForce RTX 4070 Founders Edition", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 200,
     "power_connector": ["16-pin (12VHPWR)"], "PassMark_G3D": 28000},
    {"name": "ASUS TUF RTX 4070", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 215,
     "power_connector": ["16-pin (12VHPWR)"], "PassMark_G3D": 28300},
    {"name": "Gigabyte Windforce RTX 4070", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 200,
     "power_connector": ["16-pin (12VHPWR)"], "PassMark_G3D": 28000},
    {"name": "ZOTAC Twin Edge RTX 4070", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 200,
     "power_connector": ["16-pin (12VHPWR)"], "PassMark_G3D": 27800},

    {"name": "NVIDIA GeForce RTX 4060 Ti 16GB", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 165,
     "power_connector": ["8-pin"], "PassMark_G3D": 24000},
    {"name": "ASUS Dual RTX 4060 Ti OC", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 180,
     "power_connector": ["8-pin"], "PassMark_G3D": 24500},
    {"name": "MSI Gaming X RTX 4060 Ti", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 175,
     "power_connector": ["8-pin"], "PassMark_G3D": 24200},
    {"name": "Gigabyte AERO OC RTX 4060 Ti", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 175,
     "power_connector": ["8-pin"], "PassMark_G3D": 24300},

    {"name": "NVIDIA GeForce RTX 4060", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 115,
     "power_connector": ["8-pin"], "PassMark_G3D": 20000},
    {"name": "ASUS Dual RTX 4060", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 125, "power_connector": ["8-pin"], "PassMark_G3D": 20500},
    {"name": "ZOTAC Twin Edge RTX 4060", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 115,
     "power_connector": ["8-pin"], "PassMark_G3D": 20000},
    {"name": "Gigabyte Windforce RTX 4060", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 115,
     "power_connector": ["8-pin"], "PassMark_G3D": 19800},

    {"name": "NVIDIA GeForce RTX 4050 Founders Edition", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 90,
     "power_connector": ["PCIe (no external)"], "PassMark_G3D": 16000},
    {"name": "ASUS Dual RTX 4050 OC", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 100,
     "power_connector": ["6-pin"], "PassMark_G3D": 16500},
    {"name": "MSI Ventus 2X RTX 4050", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 95,
     "power_connector": ["6-pin"], "PassMark_G3D": 16200},
    {"name": "Gigabyte Windforce RTX 4050", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 90,
     "power_connector": ["PCIe (no external)"], "PassMark_G3D": 16000},
    {"name": "ZOTAC Twin Edge RTX 4050", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 90,
     "power_connector": ["PCIe (no external)"], "PassMark_G3D": 15800},

    # AMD RX 7000 Series (Actual Benchmarks)
    {"name": "AMD Radeon RX 7900 XTX 24GB", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 355,
     "power_connector": ["8-pin", "8-pin", "8-pin"], "PassMark_G3D": 38000},
    {"name": "Sapphire Nitro+ RX 7900 XTX", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 375,
     "power_connector": ["8-pin", "8-pin", "8-pin"], "PassMark_G3D": 38500},
    {"name": "ASUS TUF Gaming RX 7900 XTX OC", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 370,
     "power_connector": ["8-pin", "8-pin", "8-pin"], "PassMark_G3D": 38300},
    {"name": "PowerColor Red Devil RX 7900 XTX", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 375,
     "power_connector": ["8-pin", "8-pin", "8-pin"], "PassMark_G3D": 38400},

    {"name": "AMD Radeon RX 7900 XT 20GB", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 300,
     "power_connector": ["8-pin", "8-pin"], "PassMark_G3D": 35000},
    {"name": "XFX Speedster MERC310 RX 7900 XT", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 315,
     "power_connector": ["8-pin", "8-pin", "8-pin"], "PassMark_G3D": 35500},
    {"name": "ASUS TUF Gaming RX 7900 XT", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 310,
     "power_connector": ["8-pin", "8-pin"], "PassMark_G3D": 35200},
    {"name": "Sapphire Pulse RX 7900 XT", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 300,
     "power_connector": ["8-pin", "8-pin"], "PassMark_G3D": 35000},

    {"name": "AMD Radeon RX 7800 XT 16GB", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 263,
     "power_connector": ["8-pin", "8-pin"], "PassMark_G3D": 32000},
    {"name": "Sapphire Nitro+ RX 7800 XT", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 280,
     "power_connector": ["8-pin", "8-pin"], "PassMark_G3D": 32500},
    {"name": "PowerColor Hellhound RX 7800 XT", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 275,
     "power_connector": ["8-pin", "8-pin"], "PassMark_G3D": 32200},
    {"name": "XFX QICK319 RX 7800 XT", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 270,
     "power_connector": ["8-pin", "8-pin"], "PassMark_G3D": 32000},

    {"name": "AMD Radeon RX 7700 XT 12GB", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 245,
     "power_connector": ["8-pin", "8-pin"], "PassMark_G3D": 30000},
    {"name": "ASRock Phantom Gaming RX 7700 XT", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 260,
     "power_connector": ["8-pin", "8-pin"], "PassMark_G3D": 30500},
    {"name": "Sapphire Pulse RX 7700 XT", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 250,
     "power_connector": ["8-pin", "8-pin"], "PassMark_G3D": 30200},
    {"name": "PowerColor Red Devil RX 7700 XT", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 260,
     "power_connector": ["8-pin", "8-pin"], "PassMark_G3D": 30400},

    {"name": "AMD Radeon RX 7600 XT 16GB", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 190,
     "power_connector": ["8-pin"], "PassMark_G3D": 26000},
    {"name": "Sapphire Pulse RX 7600 XT", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 200,
     "power_connector": ["8-pin"], "PassMark_G3D": 26500},
    {"name": "XFX Speedster SWFT210 RX 7600 XT", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 195,
     "power_connector": ["8-pin"], "PassMark_G3D": 26200},
    {"name": "PowerColor Fighter RX 7600 XT", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 190,
     "power_connector": ["8-pin"], "PassMark_G3D": 26000},

    {"name": "AMD Radeon RX 7600 8GB", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 165,
     "power_connector": ["8-pin"], "PassMark_G3D": 24000},
    {"name": "ASRock Challenger RX 7600", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 170,
     "power_connector": ["8-pin"], "PassMark_G3D": 24200},
    {"name": "XFX Speedster SWFT210 RX 7600", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 165,
     "power_connector": ["8-pin"], "PassMark_G3D": 24000},
    {"name": "PowerColor Fighter RX 7600", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 165,
     "power_connector": ["8-pin"], "PassMark_G3D": 23800},
    {"name": "Sapphire Pulse RX 7600", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 165,
     "power_connector": ["8-pin"], "PassMark_G3D": 24000},
    {"name": "Gigabyte Gaming OC RX 7600", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 170,
     "power_connector": ["8-pin"], "PassMark_G3D": 24100},
    {"name": "MSI Mech 2X RX 7600", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 170, "power_connector": ["8-pin"], "PassMark_G3D": 23900},

    # AMD RX 6000 Series (Actual Benchmarks)
    {"name": "AMD Radeon RX 6950 XT 16GB", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 335,
     "power_connector": ["8-pin", "8-pin", "8-pin"], "PassMark_G3D": 34000},
    {"name": "ASUS ROG Strix RX 6950 XT OC", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 350,
     "power_connector": ["8-pin", "8-pin", "8-pin"], "PassMark_G3D": 34500},
    {"name": "MSI Gaming X Trio RX 6950 XT", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 345,
     "power_connector": ["8-pin", "8-pin", "8-pin"], "PassMark_G3D": 34300},

    {"name": "AMD Radeon RX 6900 XT 16GB", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 300,
     "power_connector": ["8-pin", "8-pin"], "PassMark_G3D": 32000},
    {"name": "PowerColor Red Devil RX 6900 XT", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 315,
     "power_connector": ["8-pin", "8-pin", "8-pin"], "PassMark_G3D": 32500},
    {"name": "XFX MERC319 RX 6900 XT", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 310,
     "power_connector": ["8-pin", "8-pin", "8-pin"], "PassMark_G3D": 32200},

    {"name": "AMD Radeon RX 6800 XT 16GB", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 300,
     "power_connector": ["8-pin", "8-pin"], "PassMark_G3D": 31000},
    {"name": "Sapphire Nitro+ RX 6800 XT", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 315,
     "power_connector": ["8-pin", "8-pin", "8-pin"], "PassMark_G3D": 31500},
    {"name": "Gigabyte Gaming OC RX 6800 XT", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 310,
     "power_connector": ["8-pin", "8-pin", "8-pin"], "PassMark_G3D": 31200},

    {"name": "AMD Radeon RX 6750 XT 12GB", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 250,
     "power_connector": ["8-pin", "8-pin"], "PassMark_G3D": 28000},
    {"name": "ASUS Dual RX 6750 XT", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 260,
     "power_connector": ["8-pin", "8-pin"], "PassMark_G3D": 28300},
    {"name": "PowerColor Hellhound RX 6750 XT", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 255,
     "power_connector": ["8-pin", "8-pin"], "PassMark_G3D": 28100},

    {"name": "AMD Radeon RX 6700 XT 12GB", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 230,
     "power_connector": ["8-pin", "8-pin"], "PassMark_G3D": 26000},
    {"name": "Sapphire Pulse RX 6700 XT", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 240,
     "power_connector": ["8-pin", "8-pin"], "PassMark_G3D": 26300},
    {"name": "XFX Speedster QICK RX 6700 XT", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 235,
     "power_connector": ["8-pin", "8-pin"], "PassMark_G3D": 26100},

    {"name": "AMD Radeon RX 6650 XT 8GB", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 180,
     "power_connector": ["8-pin"], "PassMark_G3D": 22000},
    {"name": "MSI Mech 2X RX 6650 XT", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 190,
     "power_connector": ["8-pin"], "PassMark_G3D": 22300},
    {"name": "Sapphire Pulse RX 6650 XT", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 185,
     "power_connector": ["8-pin"], "PassMark_G3D": 22100},

    {"name": "AMD Radeon RX 6600 XT 8GB", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 160,
     "power_connector": ["8-pin"], "PassMark_G3D": 20000},
    {"name": "ASRock Phantom Gaming RX 6600 XT", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 170,
     "power_connector": ["8-pin"], "PassMark_G3D": 20300},
    {"name": "XFX SWFT 210 RX 6600 XT", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 165,
     "power_connector": ["8-pin"], "PassMark_G3D": 20100},

    {"name": "AMD Radeon RX 6600 8GB", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 132,
     "power_connector": ["8-pin"], "PassMark_G3D": 18000},
    {"name": "PowerColor Fighter RX 6600", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 140,
     "power_connector": ["8-pin"], "PassMark_G3D": 18300},
    {"name": "Sapphire Pulse RX 6600", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 135,
     "power_connector": ["8-pin"], "PassMark_G3D": 18100},

    {"name": "AMD Radeon RX 6500 XT 4GB", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 107,
     "power_connector": ["6-pin"], "PassMark_G3D": 12000},
    {"name": "ASUS Dual RX 6500 XT", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 115, "power_connector": ["6-pin"], "PassMark_G3D": 12300},
    {"name": "Sapphire Pulse RX 6500 XT", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 110,
     "power_connector": ["6-pin"], "PassMark_G3D": 12100},

    {"name": "AMD Radeon RX 6400 4GB", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 53,
     "power_connector": ["PCIe (no external)"], "PassMark_G3D": 8000},
    {"name": "ASRock Challenger RX 6400", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 55,
     "power_connector": ["PCIe (no external)"], "PassMark_G3D": 8100},
    {"name": "PowerColor RX 6400 ITX", "PCIe_Gen": "PCIe 4.0", "Power_Needed": 53,
     "power_connector": ["PCIe (no external)"], "PassMark_G3D": 8000}
]

PartSpec.objects.get_or_create(name="PCIe_Gen",part=GPU_part)
PartSpec.objects.get_or_create(name="Power_Needed",part=GPU_part)
PartSpec.objects.get_or_create(name="power_connector",part=GPU_part)
PartSpec.objects.get_or_create(name="PassMark_G3D",part=GPU_part)


PCIe_Gen=PartSpec.objects.get(name="PCIe_Gen",part=GPU_part)
Power_Needed=PartSpec.objects.get(name="Power_Needed",part=GPU_part)
power_connector=PartSpec.objects.get(name="power_connector",part=GPU_part)
PassMark_G3D=PartSpec.objects.get(name="PassMark_G3D",part=GPU_part)


for product in gpu_specs:
    THEproduct=Product.objects.get(name=product["name"])
    ProductSpec.objects.get_or_create(product=THEproduct,part_spec=PCIe_Gen,value=product["PCIe_Gen"])
    ProductSpec.objects.get_or_create(product=THEproduct, part_spec=Power_Needed, value=product["Power_Needed"])
    ProductSpec.objects.get_or_create(product=THEproduct, part_spec=power_connector, value=product["power_connector"])
    ProductSpec.objects.get_or_create(product=THEproduct, part_spec=PassMark_G3D, value=product["PassMark_G3D"])








