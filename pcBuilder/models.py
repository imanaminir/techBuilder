from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models

class Part(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Spec(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class PartSpec(models.Model):
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    spec = models.ForeignKey(Spec, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.part.name} - {self.spec.name}"


class Product(models.Model):
    name = models.CharField(max_length=255)
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    brand = models.CharField(max_length=255)  # یا اگر جدول Brand دارید بعداً ForeignKey کنید
    price = models.DecimalField(max_digits=12, decimal_places=0)

    def __str__(self):
        return self.name



class ProductSpec(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    part_spec = models.ForeignKey(PartSpec, on_delete=models.CASCADE)
    value = models.TextField()

    def __str__(self):
        return f"{self.product.name} - {self.part_spec.spec.name}: {self.value}"


class CompatibilityCheck(models.Model):
    partSpec_1 = models.ForeignKey(PartSpec, on_delete=models.CASCADE, related_name='compat_partspec_1')
    partSpec_2 = models.ForeignKey(PartSpec, on_delete=models.CASCADE, related_name='compat_partspec_2')

    def __str__(self):
        return f"{self.partSpec_1.part.name} ({self.partSpec_1.spec.name}) vs {self.partSpec_2.part.name} ({self.partSpec_2.spec.name})"

class Build(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    input= models.JSONField()
    partPercentage = models.JSONField()
    budget = models.DecimalField(max_digits=12, decimal_places=0)
    star = models.BooleanField(default=False)
    Cpu= models.ForeignKey(Product, on_delete=models.PROTECT, related_name='cpu')
    MotherBoard= models.ForeignKey(Product, on_delete=models.PROTECT, related_name='motherboard')
    Ram= models.ForeignKey(Product, on_delete=models.PROTECT, related_name='ram')
    Gpu= models.ForeignKey(Product, on_delete=models.PROTECT, related_name='gpu')
    CpuCooler= models.ForeignKey(Product, on_delete=models.PROTECT, related_name='cpuCooler')
    Monitor= models.ForeignKey(Product, on_delete=models.PROTECT, related_name='monitor')
    Power= models.ForeignKey(Product, on_delete=models.PROTECT, related_name='power')

    def __str__(self):
        return f"{self.user} - {self.id}"

