import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'techBuilder.settings')
django.setup()

from pcBuilder.models import Product, Part, PartSpec,ProductSpec
Part.objects.get_or_create(name="MotherBoard")
motherBoard_part = Part.objects.get(name="MotherBoard")



motherBoards =[

    {"name": "ASUS ROG MAXIMUS Z790 HERO","brand": "ASUS","price" :599},
    {"name": "ASUS TUF Gaming Z790-PLUS WIFI D4","brand": "ASUS","price" :269},
    {"name": "ASUS PRIME Z790-P WIFI","brand": "ASUS","price" :209},
    {"name": "MSI MEG Z790 GODLIKE","brand": "MSI","price" :699},
    {"name": "MSI MPG Z790 CARBON WIFI","brand": "MSI","price" :409},
    {"name": "MSI PRO Z790-A WIFI","brand": "MSI","price" :229},
    {"name": "Gigabyte Z790 AORUS MASTER","brand": "Gigabyte","price" :449},
    {"name": "Gigabyte Z790 AORUS ELITE AX","brand": "Gigabyte","price" :269},
    {"name": "Gigabyte Z790 UD AC","brand": "Gigabyte","price" :189},
    {"name": "ASRock Z790 Taichi","brand": "ASRock","price" :369},
    {"name": "ASRock Z790 PG Lightning","brand": "ASRock","price" :209},
    {"name": "ASRock Z790 Steel Legend WIFI","brand": "ASRock","price" :249},


    {"name": "ASUS TUF Gaming B760-PLUS WIFI D4","brand": "ASUS","price" :195},
    {"name": "ASUS PRIME B760M-A WIFI D4","brand": "ASUS","price" :165},
    {"name": "ASUS ROG STRIX B760-F GAMING WIFI","brand": "ASUS","price" :225},
    {"name": "MSI PRO B760M-A WIFI DDR4","brand": "MSI","price" :145},
    {"name": "MSI MAG B760 TOMAHAWK WIFI","brand": "MSI","price" :215},
    {"name": "MSI MPG B760I EDGE WIFI DDR4","brand": "MSI","price" :189},
    {"name": "Gigabyte B760 AORUS ELITE AX","brand": "Gigabyte","price" :199},
    {"name": "ASRock B760M Steel Legend WIFI","brand": "ASRock","price" :175},


    {"name": "ASUS ROG MAXIMUS Z690 HERO","brand": "ASUS","price" :549},
    {"name": "ASUS TUF Gaming Z690-PLUS WIFI D4","brand": "ASUS","price" :255},
    {"name": "MSI MPG Z690 CARBON WIFI","brand": "MSI","price" :379},
    {"name": "Gigabyte Z690 AORUS ELITE AX DDR4","brand": "Gigabyte","price" :239},
    {"name": "ASRock Z690 Extreme WIFI 6E","brand": "ASRock","price" :269},


    {"name": "ASUS PRIME B660M-A WIFI D4","brand": "ASUS","price" :145},
    {"name": "MSI PRO B660M-A WIFI DDR4","brand": "MSI","price" :135},
    {"name": "Gigabyte B660M DS3H AX DDR4","brand": "Gigabyte","price" :129},
    {"name": "ASRock B660M Pro RS","brand": "ASRock","price" :119},


    {"name": "ASUS ROG MAXIMUS XIII HERO Z590","brand": "ASUS","price" :439},
    {"name": "MSI MPG Z590 GAMING EDGE WIFI","brand": "MSI","price" :289},
    {"name": "Gigabyte Z590 AORUS ELITE AX","brand": "Gigabyte","price" :269},
    {"name": "ASRock Z590 Extreme WIFI 6E","brand": "ASRock","price" :239},


    {"name": "MSI B560M PRO-VDH WIFI","brand": "MSI","price" :115},
    {"name": "Gigabyte B560M DS3H AC","brand": "Gigabyte","price" :109},
    {"name": "ASRock B560M Steel Legend","brand": "ASRock","price" :119},


    {"name": "ASUS ROG CROSSHAIR X670E HERO","brand": "ASUS","price" :519},
    {"name": "ASUS PRIME X670-P WIFI","brand": "ASUS","price" :289},
    {"name": "ASUS TUF Gaming X670E-PLUS WIFI","brand": "ASUS","price" :319},
    {"name": "MSI MEG X670E ACE","brand": "MSI","price" :489},
    {"name": "Gigabyte X670 AORUS ELITE AX","brand": "Gigabyte","price" :309},
    {"name": "Gigabyte X670E AORUS MASTER","brand": "Gigabyte","price" :449},
    {"name": "ASRock X670E Steel Legend","brand": "ASRock","price" :319},
    {"name": "ASRock X670E Pro RS","brand": "ASRock","price" :279},




    {"name": "ASUS PRIME B650M-A WIFI","brand": "ASUS","price" :189},
    {"name": "MSI PRO B650M-A WIFI","brand": "MSI","price" :179},
    {"name": "MSI MAG B650 TOMAHAWK WIFI","brand": "MSI","price" :219},
    {"name": "Gigabyte B650 AORUS ELITE AX","brand": "Gigabyte","price" :229},
    {"name": "Gigabyte B650M DS3H AX","brand": "Gigabyte","price" :179},
    {"name": "ASRock B650 PG Lightning","brand": "ASRock","price" :199},
    {"name": "ASRock B650M Pro RS","brand": "ASRock","price" :169},


    {"name": "ASUS ROG CROSSHAIR VIII HERO (WI-FI)","brand": "ASUS","price" :359},
    {"name": "ASUS PRIME X570-PRO","brand": "ASUS","price" :259},
    {"name": "ASUS TUF Gaming X570-PLUS WIFI","brand": "ASUS","price" :219},
    {"name": "MSI MEG X570 ACE","brand": "MSI","price" :379},
    {"name": "MSI MPG X570 GAMING EDGE WIFI","brand": "MSI","price" :239},
    {"name": "MSI MAG X570 TOMAHAWK WIFI","brand": "MSI","price" :249},
    {"name": "Gigabyte X570 AORUS MASTER","brand": "Gigabyte","price" :349},
    {"name": "Gigabyte X570 AORUS ELITE WIFI","brand": "Gigabyte","price" :219},
    {"name": "ASRock X570 Steel Legend","brand": "ASRock","price" :219},
    {"name": "ASRock X570 Phantom Gaming 4","brand": "ASRock","price" :189},


    {"name": "ASUS PRIME B550M-A WIFI II","brand": "ASUS","price" :179},
    {"name": "MSI B550M PRO-VDH WIFI","brand": "MSI","price" :149},
    {"name": "MSI MPG B550 GAMING PLUS","brand": "MSI","price" :179},
    {"name": "Gigabyte B550M DS3H AC","brand": "Gigabyte","price" :139},
    {"name": "ASRock B550 Phantom Gaming 4","brand": "ASRock","price" :149},

]

for motherBoard in motherBoards:
    Product.objects.get_or_create(
        name=motherBoard["name"],
        part=motherBoard_part,
        brand=motherBoard["brand"],
        price=motherBoard["price"]
    )


MB_specs=[
    # Intel Z790 Motherboards
    {"name": "ASUS ROG MAXIMUS Z790 HERO", "CPU_GENs_Supported": ["Intel 12", "Intel 13", "Intel 14"], "RAM_GEN_Supported": ["DDR5"], "PCIe_GENs": ["PCIe 5.0", "PCIe 4.0"], "Power_Connector": ["24-pin ATX", "8-pin EPS", "4-pin EPS"]},
    {"name": "ASUS TUF Gaming Z790-PLUS WIFI D4", "CPU_GENs_Supported": ["Intel 12", "Intel 13", "Intel 14"], "RAM_GEN_Supported": ["DDR4"], "PCIe_GENs": ["PCIe 5.0", "PCIe 4.0"], "Power_Connector": ["24-pin ATX", "8-pin EPS"]},
    {"name": "ASUS PRIME Z790-P WIFI", "CPU_GENs_Supported": ["Intel 12", "Intel 13", "Intel 14"], "RAM_GEN_Supported": ["DDR5"], "PCIe_GENs": ["PCIe 5.0", "PCIe 4.0"], "Power_Connector": ["24-pin ATX", "8-pin EPS"]},
    {"name": "MSI MEG Z790 GODLIKE", "CPU_GENs_Supported": ["Intel 12", "Intel 13", "Intel 14"], "RAM_GEN_Supported": ["DDR5"], "PCIe_GENs": ["PCIe 5.0", "PCIe 4.0"], "Power_Connector": ["24-pin ATX", "8-pin EPS", "8-pin EPS", "6-pin PCIe"]},
    {"name": "MSI MPG Z790 CARBON WIFI", "CPU_GENs_Supported": ["Intel 12", "Intel 13", "Intel 14"], "RAM_GEN_Supported": ["DDR5"], "PCIe_GENs": ["PCIe 5.0", "PCIe 4.0"], "Power_Connector": ["24-pin ATX", "8-pin EPS", "4-pin EPS"]},
    {"name": "MSI PRO Z790-A WIFI", "CPU_GENs_Supported": ["Intel 12", "Intel 13", "Intel 14"], "RAM_GEN_Supported": ["DDR5"], "PCIe_GENs": ["PCIe 5.0", "PCIe 4.0"], "Power_Connector": ["24-pin ATX", "8-pin EPS"]},
    {"name": "Gigabyte Z790 AORUS MASTER", "CPU_GENs_Supported": ["Intel 12", "Intel 13", "Intel 14"], "RAM_GEN_Supported": ["DDR5"], "PCIe_GENs": ["PCIe 5.0", "PCIe 4.0"], "Power_Connector": ["24-pin ATX", "8-pin EPS", "8-pin EPS"]},
    {"name": "Gigabyte Z790 AORUS ELITE AX", "CPU_GENs_Supported": ["Intel 12", "Intel 13", "Intel 14"], "RAM_GEN_Supported": ["DDR5"], "PCIe_GENs": ["PCIe 5.0", "PCIe 4.0"], "Power_Connector": ["24-pin ATX", "8-pin EPS"]},
    {"name": "Gigabyte Z790 UD AC", "CPU_GENs_Supported": ["Intel 12", "Intel 13", "Intel 14"], "RAM_GEN_Supported": ["DDR4"], "PCIe_GENs": ["PCIe 5.0", "PCIe 4.0"], "Power_Connector": ["24-pin ATX", "8-pin EPS"]},
    {"name": "ASRock Z790 Taichi", "CPU_GENs_Supported": ["Intel 12", "Intel 13", "Intel 14"], "RAM_GEN_Supported": ["DDR5"], "PCIe_GENs": ["PCIe 5.0", "PCIe 4.0"], "Power_Connector": ["24-pin ATX", "8-pin EPS", "8-pin EPS"]},
    {"name": "ASRock Z790 PG Lightning", "CPU_GENs_Supported": ["Intel 12", "Intel 13", "Intel 14"], "RAM_GEN_Supported": ["DDR5"], "PCIe_GENs": ["PCIe 5.0", "PCIe 4.0"], "Power_Connector": ["24-pin ATX", "8-pin EPS"]},
    {"name": "ASRock Z790 Steel Legend WIFI", "CPU_GENs_Supported": ["Intel 12", "Intel 13", "Intel 14"], "RAM_GEN_Supported": ["DDR5"], "PCIe_GENs": ["PCIe 5.0", "PCIe 4.0"], "Power_Connector": ["24-pin ATX", "8-pin EPS"]},

    # Intel B760 Motherboards
    {"name": "ASUS TUF Gaming B760-PLUS WIFI D4", "CPU_GENs_Supported": ["Intel 12", "Intel 13", "Intel 14"], "RAM_GEN_Supported": ["DDR4"], "PCIe_GENs": ["PCIe 5.0", "PCIe 4.0"], "Power_Connector": ["24-pin ATX", "8-pin EPS"]},
    {"name": "ASUS PRIME B760M-A WIFI D4", "CPU_GENs_Supported": ["Intel 12", "Intel 13", "Intel 14"], "RAM_GEN_Supported": ["DDR4"], "PCIe_GENs": ["PCIe 5.0", "PCIe 4.0"], "Power_Connector": ["24-pin ATX", "8-pin EPS"]},
    {"name": "ASUS ROG STRIX B760-F GAMING WIFI", "CPU_GENs_Supported": ["Intel 12", "Intel 13", "Intel 14"], "RAM_GEN_Supported": ["DDR5"], "PCIe_GENs": ["PCIe 5.0", "PCIe 4.0"], "Power_Connector": ["24-pin ATX", "8-pin EPS"]},
    {"name": "MSI PRO B760M-A WIFI DDR4", "CPU_GENs_Supported": ["Intel 12", "Intel 13", "Intel 14"], "RAM_GEN_Supported": ["DDR4"], "PCIe_GENs": ["PCIe 5.0", "PCIe 4.0"], "Power_Connector": ["24-pin ATX", "8-pin EPS"]},
    {"name": "MSI MAG B760 TOMAHAWK WIFI", "CPU_GENs_Supported": ["Intel 12", "Intel 13", "Intel 14"], "RAM_GEN_Supported": ["DDR5"], "PCIe_GENs": ["PCIe 5.0", "PCIe 4.0"], "Power_Connector": ["24-pin ATX", "8-pin EPS"]},
    {"name": "MSI MPG B760I EDGE WIFI DDR4", "CPU_GENs_Supported": ["Intel 12", "Intel 13", "Intel 14"], "RAM_GEN_Supported": ["DDR4"], "PCIe_GENs": ["PCIe 5.0", "PCIe 4.0"], "Power_Connector": ["24-pin ATX", "8-pin EPS"]},
    {"name": "Gigabyte B760 AORUS ELITE AX", "CPU_GENs_Supported": ["Intel 12", "Intel 13", "Intel 14"], "RAM_GEN_Supported": ["DDR5"], "PCIe_GENs": ["PCIe 5.0", "PCIe 4.0"], "Power_Connector": ["24-pin ATX", "8-pin EPS"]},
    {"name": "ASRock B760M Steel Legend WIFI", "CPU_GENs_Supported": ["Intel 12", "Intel 13", "Intel 14"], "RAM_GEN_Supported": ["DDR5"], "PCIe_GENs": ["PCIe 5.0", "PCIe 4.0"], "Power_Connector": ["24-pin ATX", "8-pin EPS"]},

    # Intel Z690 Motherboards
    {"name": "ASUS ROG MAXIMUS Z690 HERO", "CPU_GENs_Supported": ["Intel 12", "Intel 13"], "RAM_GEN_Supported": ["DDR5"], "PCIe_GENs": ["PCIe 5.0", "PCIe 4.0"], "Power_Connector": ["24-pin ATX", "8-pin EPS", "4-pin EPS"]},
    {"name": "ASUS TUF Gaming Z690-PLUS WIFI D4", "CPU_GENs_Supported": ["Intel 12", "Intel 13"], "RAM_GEN_Supported": ["DDR4"], "PCIe_GENs": ["PCIe 5.0", "PCIe 4.0"], "Power_Connector": ["24-pin ATX", "8-pin EPS"]},
    {"name": "MSI MPG Z690 CARBON WIFI", "CPU_GENs_Supported": ["Intel 12", "Intel 13"], "RAM_GEN_Supported": ["DDR5"], "PCIe_GENs": ["PCIe 5.0", "PCIe 4.0"], "Power_Connector": ["24-pin ATX", "8-pin EPS", "4-pin EPS"]},
    {"name": "Gigabyte Z690 AORUS ELITE AX DDR4", "CPU_GENs_Supported": ["Intel 12", "Intel 13"], "RAM_GEN_Supported": ["DDR4"], "PCIe_GENs": ["PCIe 5.0", "PCIe 4.0"], "Power_Connector": ["24-pin ATX", "8-pin EPS"]},
    {"name": "ASRock Z690 Extreme WIFI 6E", "CPU_GENs_Supported": ["Intel 12", "Intel 13"], "RAM_GEN_Supported": ["DDR5"], "PCIe_GENs": ["PCIe 5.0", "PCIe 4.0"], "Power_Connector": ["24-pin ATX", "8-pin EPS"]},

    # Intel B660 Motherboards
    {"name": "ASUS PRIME B660M-A WIFI D4", "CPU_GENs_Supported": ["Intel 12", "Intel 13"], "RAM_GEN_Supported": ["DDR4"], "PCIe_GENs": ["PCIe 5.0", "PCIe 4.0"], "Power_Connector": ["24-pin ATX", "8-pin EPS"]},
    {"name": "MSI PRO B660M-A WIFI DDR4", "CPU_GENs_Supported": ["Intel 12", "Intel 13"], "RAM_GEN_Supported": ["DDR4"], "PCIe_GENs": ["PCIe 5.0", "PCIe 4.0"], "Power_Connector": ["24-pin ATX", "8-pin EPS"]},
    {"name": "Gigabyte B660M DS3H AX DDR4", "CPU_GENs_Supported": ["Intel 12", "Intel 13"], "RAM_GEN_Supported": ["DDR4"], "PCIe_GENs": ["PCIe 5.0", "PCIe 4.0"], "Power_Connector": ["24-pin ATX", "8-pin EPS"]},
    {"name": "ASRock B660M Pro RS", "CPU_GENs_Supported": ["Intel 12", "Intel 13"], "RAM_GEN_Supported": ["DDR4"], "PCIe_GENs": ["PCIe 5.0", "PCIe 4.0"], "Power_Connector": ["24-pin ATX", "8-pin EPS"]},

    # AMD X670E/X670 Motherboards
    {"name": "ASUS ROG CROSSHAIR X670E HERO", "CPU_GENs_Supported": ["AMD 5"], "RAM_GEN_Supported": ["DDR5"], "PCIe_GENs": ["PCIe 5.0", "PCIe 4.0"], "Power_Connector": ["24-pin ATX", "8-pin EPS", "8-pin EPS"]},
    {"name": "ASUS PRIME X670-P WIFI", "CPU_GENs_Supported": ["AMD 5"], "RAM_GEN_Supported": ["DDR5"], "PCIe_GENs": ["PCIe 5.0", "PCIe 4.0"], "Power_Connector": ["24-pin ATX", "8-pin EPS", "4-pin EPS"]},
    {"name": "ASUS TUF Gaming X670E-PLUS WIFI", "CPU_GENs_Supported": ["AMD 5"], "RAM_GEN_Supported": ["DDR5"], "PCIe_GENs": ["PCIe 5.0", "PCIe 4.0"], "Power_Connector": ["24-pin ATX", "8-pin EPS", "8-pin EPS"]},
    {"name": "MSI MEG X670E ACE", "CPU_GENs_Supported": ["AMD 5"], "RAM_GEN_Supported": ["DDR5"], "PCIe_GENs": ["PCIe 5.0", "PCIe 4.0"], "Power_Connector": ["24-pin ATX", "8-pin EPS", "8-pin EPS"]},
    {"name": "Gigabyte X670 AORUS ELITE AX", "CPU_GENs_Supported": ["AMD 5"], "RAM_GEN_Supported": ["DDR5"], "PCIe_GENs": ["PCIe 5.0", "PCIe 4.0"], "Power_Connector": ["24-pin ATX", "8-pin EPS", "4-pin EPS"]},
    {"name": "Gigabyte X670E AORUS MASTER", "CPU_GENs_Supported": ["AMD 5"], "RAM_GEN_Supported": ["DDR5"], "PCIe_GENs": ["PCIe 5.0", "PCIe 4.0"], "Power_Connector": ["24-pin ATX", "8-pin EPS", "8-pin EPS"]},
    {"name": "ASRock X670E Steel Legend", "CPU_GENs_Supported": ["AMD 5"], "RAM_GEN_Supported": ["DDR5"], "PCIe_GENs": ["PCIe 5.0", "PCIe 4.0"], "Power_Connector": ["24-pin ATX", "8-pin EPS", "8-pin EPS"]},
    {"name": "ASRock X670E Pro RS", "CPU_GENs_Supported": ["AMD 5"], "RAM_GEN_Supported": ["DDR5"], "PCIe_GENs": ["PCIe 5.0", "PCIe 4.0"], "Power_Connector": ["24-pin ATX", "8-pin EPS", "4-pin EPS"]},

    # AMD B650 Motherboards
    {"name": "ASUS PRIME B650M-A WIFI", "CPU_GENs_Supported": ["AMD 5"], "RAM_GEN_Supported": ["DDR5"], "PCIe_GENs": ["PCIe 5.0", "PCIe 4.0"], "Power_Connector": ["24-pin ATX", "8-pin EPS"]},
    {"name": "MSI PRO B650M-A WIFI", "CPU_GENs_Supported": ["AMD 5"], "RAM_GEN_Supported": ["DDR5"], "PCIe_GENs": ["PCIe 5.0", "PCIe 4.0"], "Power_Connector": ["24-pin ATX", "8-pin EPS"]},
    {"name": "MSI MAG B650 TOMAHAWK WIFI", "CPU_GENs_Supported": ["AMD 5"], "RAM_GEN_Supported": ["DDR5"], "PCIe_GENs": ["PCIe 5.0", "PCIe 4.0"], "Power_Connector": ["24-pin ATX", "8-pin EPS"]},
    {"name": "Gigabyte B650 AORUS ELITE AX", "CPU_GENs_Supported": ["AMD 5"], "RAM_GEN_Supported": ["DDR5"], "PCIe_GENs": ["PCIe 5.0", "PCIe 4.0"], "Power_Connector": ["24-pin ATX", "8-pin EPS"]},
    {"name": "Gigabyte B650M DS3H AX", "CPU_GENs_Supported": ["AMD 5"], "RAM_GEN_Supported": ["DDR5"], "PCIe_GENs": ["PCIe 5.0", "PCIe 4.0"], "Power_Connector": ["24-pin ATX", "8-pin EPS"]},
    {"name": "ASRock B650 PG Lightning", "CPU_GENs_Supported": ["AMD 5"], "RAM_GEN_Supported": ["DDR5"], "PCIe_GENs": ["PCIe 5.0", "PCIe 4.0"], "Power_Connector": ["24-pin ATX", "8-pin EPS"]},
    {"name": "ASRock B650M Pro RS", "CPU_GENs_Supported": ["AMD 5"], "RAM_GEN_Supported": ["DDR5"], "PCIe_GENs": ["PCIe 5.0", "PCIe 4.0"], "Power_Connector": ["24-pin ATX", "8-pin EPS"]},

    # AMD X570 Motherboards
    {"name": "ASUS ROG CROSSHAIR VIII HERO (WI-FI)", "CPU_GENs_Supported": ["AMD 3", "AMD 4"], "RAM_GEN_Supported": ["DDR4"], "PCIe_GENs": ["PCIe 4.0"], "Power_Connector": ["24-pin ATX", "8-pin EPS", "4-pin EPS"]},
    {"name": "ASUS PRIME X570-PRO", "CPU_GENs_Supported": ["AMD 3", "AMD 4"], "RAM_GEN_Supported": ["DDR4"], "PCIe_GENs": ["PCIe 4.0"], "Power_Connector": ["24-pin ATX", "8-pin EPS"]},
    {"name": "ASUS TUF Gaming X570-PLUS WIFI", "CPU_GENs_Supported": ["AMD 3", "AMD 4"], "RAM_GEN_Supported": ["DDR4"], "PCIe_GENs": ["PCIe 4.0"], "Power_Connector": ["24-pin ATX", "8-pin EPS"]},
    {"name": "MSI MEG X570 ACE", "CPU_GENs_Supported": ["AMD 3", "AMD 4"], "RAM_GEN_Supported": ["DDR4"], "PCIe_GENs": ["PCIe 4.0"], "Power_Connector": ["24-pin ATX", "8-pin EPS", "4-pin EPS"]},
    {"name": "MSI MPG X570 GAMING EDGE WIFI", "CPU_GENs_Supported": ["AMD 3", "AMD 4"], "RAM_GEN_Supported": ["DDR4"], "PCIe_GENs": ["PCIe 4.0"], "Power_Connector": ["24-pin ATX", "8-pin EPS"]},
    {"name": "MSI MAG X570 TOMAHAWK WIFI", "CPU_GENs_Supported": ["AMD 3", "AMD 4"], "RAM_GEN_Supported": ["DDR4"], "PCIe_GENs": ["PCIe 4.0"], "Power_Connector": ["24-pin ATX", "8-pin EPS"]},
    {"name": "Gigabyte X570 AORUS MASTER", "CPU_GENs_Supported": ["AMD 3", "AMD 4"], "RAM_GEN_Supported": ["DDR4"], "PCIe_GENs": ["PCIe 4.0"], "Power_Connector": ["24-pin ATX", "8-pin EPS", "4-pin EPS"]},
    {"name": "Gigabyte X570 AORUS ELITE WIFI", "CPU_GENs_Supported": ["AMD 3", "AMD 4"], "RAM_GEN_Supported": ["DDR4"], "PCIe_GENs": ["PCIe 4.0"], "Power_Connector": ["24-pin ATX", "8-pin EPS"]},
    {"name": "ASRock X570 Steel Legend", "CPU_GENs_Supported": ["AMD 3", "AMD 4"], "RAM_GEN_Supported": ["DDR4"], "PCIe_GENs": ["PCIe 4.0"], "Power_Connector": ["24-pin ATX", "8-pin EPS"]},
    {"name": "ASRock X570 Phantom Gaming 4", "CPU_GENs_Supported": ["AMD 3", "AMD 4"], "RAM_GEN_Supported": ["DDR4"], "PCIe_GENs": ["PCIe 4.0"], "Power_Connector": ["24-pin ATX", "8-pin EPS"]},

    # AMD B550 Motherboards
    {"name": "ASUS PRIME B550M-A WIFI II", "CPU_GENs_Supported": ["AMD 3", "AMD 4"], "RAM_GEN_Supported": ["DDR4"], "PCIe_GENs": ["PCIe 4.0", "PCIe 3.0"], "Power_Connector": ["24-pin ATX", "8-pin EPS"]},
    {"name": "MSI B550M PRO-VDH WIFI", "CPU_GENs_Supported": ["AMD 3", "AMD 4"], "RAM_GEN_Supported": ["DDR4"], "PCIe_GENs": ["PCIe 4.0", "PCIe 3.0"], "Power_Connector": ["24-pin ATX", "8-pin EPS"]},
    {"name": "MSI MPG B550 GAMING PLUS", "CPU_GENs_Supported": ["AMD 3", "AMD 4"], "RAM_GEN_Supported": ["DDR4"], "PCIe_GENs": ["PCIe 4.0", "PCIe 3.0"], "Power_Connector": ["24-pin ATX", "8-pin EPS"]},
    {"name": "Gigabyte B550M DS3H AC", "CPU_GENs_Supported": ["AMD 3", "AMD 4"], "RAM_GEN_Supported": ["DDR4"], "PCIe_GENs": ["PCIe 4.0", "PCIe 3.0"], "Power_Connector": ["24-pin ATX", "8-pin EPS"]},
    {"name": "ASRock B550 Phantom Gaming 4", "CPU_GENs_Supported": ["AMD 3", "AMD 4"], "RAM_GEN_Supported": ["DDR4"], "PCIe_GENs": ["PCIe 4.0", "PCIe 3.0"], "Power_Connector": ["24-pin ATX", "8-pin EPS"]}
]



PartSpec.objects.get_or_create(name="CPU_GENs_Supported",part=motherBoard_part)
PartSpec.objects.get_or_create(name="RAM_GEN_Supported",part=motherBoard_part)
PartSpec.objects.get_or_create(name="PCIe_GENs",part=motherBoard_part)
PartSpec.objects.get_or_create(name="Power_Connector",part=motherBoard_part)


CPU_GENs_Supported=PartSpec.objects.get(name="CPU_GENs_Supported",part=motherBoard_part)
RAM_GEN_Supported=PartSpec.objects.get(name="RAM_GEN_Supported",part=motherBoard_part)
PCIe_GEN=PartSpec.objects.get(name="PCIe_GENs",part=motherBoard_part)
Power_Connector=PartSpec.objects.get(name="Power_Connector",part=motherBoard_part)


for product in MB_specs:
    THEproduct=Product.objects.get(name=product["name"])
    ProductSpec.objects.get_or_create(product=THEproduct,part_spec=CPU_GENs_Supported,value=product["CPU_GENs_Supported"])
    ProductSpec.objects.get_or_create(product=THEproduct, part_spec=RAM_GEN_Supported, value=product["RAM_GEN_Supported"])
    ProductSpec.objects.get_or_create(product=THEproduct, part_spec=PCIe_GEN, value=product["PCIe_GENs"])
    ProductSpec.objects.get_or_create(product=THEproduct, part_spec=Power_Connector, value=product["Power_Connector"])























