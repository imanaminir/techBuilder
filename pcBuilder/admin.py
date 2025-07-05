from django.contrib import admin

# Register your models here.
from .models import Part, Product, PartSpec, ProductSpec, CompatibilityCheck, Build

admin.site.register(Part)
admin.site.register(PartSpec)
admin.site.register(Product)
admin.site.register(ProductSpec)
admin.site.register(CompatibilityCheck)
admin.site.register(Build)