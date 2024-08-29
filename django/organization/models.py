from django.db import models
from address.models import Address

# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    address = models.ForeignKey(Address, unique=True, on_delete=models.SET_NULL)
    area = models.CharField()
    description = models.CharField(max_length=250)
