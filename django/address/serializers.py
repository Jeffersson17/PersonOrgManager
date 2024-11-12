from .models import Address, City
from rest_framework import serializers


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['name', 'state']


class AddressSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)


    class Meta:
        model = Address
        fields = ['address', 'address_type', 'city', 'cep', 'number', 'complement']

