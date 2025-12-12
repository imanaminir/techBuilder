from django.contrib.auth.models import User

from django.db import models

class Part(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class PartSpec(models.Model):
    name = models.CharField(max_length=255)
    part = models.ForeignKey(Part, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.part.name} - {self.name}"


class Product(models.Model):
    name = models.CharField(max_length=255)
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    brand = models.CharField(max_length=255)  # یا اگر جدول Brand دارید بعداً ForeignKey کنید
    price = models.DecimalField(max_digits=12, decimal_places=0)
    def __str__(self):
        return self.name
    @property
    def spec_dict(self):
        if not hasattr(self, '_spec_dict'):
            self._spec_dict = {
                spec.part_spec.name: spec.value
                for spec in self.productspec_set.select_related('part_spec').all()
            }
        return self._spec_dict




class ProductSpec(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    part_spec = models.ForeignKey(PartSpec, on_delete=models.CASCADE)
    value = models.JSONField()

    def __str__(self):
        return f"{self.product.name} - {self.part_spec.name}: {self.value}"


class CompatibilityCheck(models.Model):
    partSpec_1 = models.ForeignKey(PartSpec, on_delete=models.CASCADE, related_name='compat_partspec_1')
    partSpec_2 = models.ForeignKey(PartSpec, on_delete=models.CASCADE, related_name='compat_partspec_2')

    def __str__(self):
        return f"{self.partSpec_1.part.name} ({self.partSpec_1.spec.name}) vs {self.partSpec_2.part.name} ({self.partSpec_2.spec.name})"


class Build(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    input = models.JSONField()
    part_percentage = models.JSONField()
    budget = models.DecimalField(max_digits=12, decimal_places=0)
    star = models.BooleanField(default=False)

    cpu = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='build_cpu', null=True, blank=True)
    motherboard = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='build_motherboard', null=True, blank=True)
    ram = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='build_ram', null=True, blank=True)
    gpu = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='build_gpu', null=True, blank=True)
    cpu_cooler = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='build_cpu_cooler', null=True, blank=True)
    monitor = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='build_monitor', null=True, blank=True)
    power = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='build_power', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - Build #{self.id}"


