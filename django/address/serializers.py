from .models import Address, City
from rest_framework import serializers


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['name', 'state']


class AddressSerializer(serializers.ModelSerializer):
    city_base = CitySerializer(read_only=True, source='city')


    class Meta:
        model = Address
        fields = ['address', 'address_type', 'city', 'city_base', 'cep', 'number', 'complement']

