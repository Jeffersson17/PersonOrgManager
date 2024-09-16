from django.db import models
from address.defaults import ADDRESS_TYPE, STATE_CITY_CHOICE


class City(models.Model):
    name = models.CharField(max_length=20)
    state = models.CharField(STATE_CITY_CHOICE, max_length=2)


    def __str__(self):
        return self.name

    
    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'
        ordering = ['name']


class Address(models.Model):
    address = models.CharField(max_length=50)
    address_type = models.CharField(ADDRESS_TYPE, max_length=2)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    cep = models.CharField(max_length=8)
    number = models.CharField(max_length=15)
    complement = models.CharField(max_length=250, blank=True, null=True)


    def __str__ (self):
        return self.address


    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'
        ordering = ['city']
