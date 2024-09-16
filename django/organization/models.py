from django.db import models
from address.models import Address
from address.defaults import AREA_CHOICES

class Organization(models.Model):
    name = models.TextField()
    phone = models.CharField(max_length=20)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    area = models.CharField(AREA_CHOICES, max_length=2)
    description = models.CharField(max_length=250, null=True, blank=True)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Organização'
        verbose_name_plural = 'Organizações'
