from .models import Organization
from rest_framework import serializers
from address.serializers import AddressSerializer

class OrganizationSerializer(serializers.ModelSerializer):
    address = AddressSerializer(read_only=True)


    class Meta:
        model = Organization
        fields = ['id', 'name', 'phone', 'address', 'area', 'description']

