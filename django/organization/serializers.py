from .models import Organization
from rest_framework import serializers
from address.serializers import AddressSerializer
from address.defaults import AREA_CHOICES, ADDRESS_TYPE, STATE_CITY_CHOICE

class OrganizationSerializer(serializers.ModelSerializer):
    address = AddressSerializer(read_only=True)


    class Meta:
        model = Organization
        fields = ['id', 'name', 'phone', 'address', 'area', 'description']


class StatusChoicesSerializer(serializers.Serializer):
    area_choices = serializers.SerializerMethodField()
    address_type = serializers.SerializerMethodField()
    state_city_choice = serializers.SerializerMethodField()


    def get_area_choices(self, obj):
        return list(AREA_CHOICES.values())


    def get_address_type(self, obj):
        return list(ADDRESS_TYPE.values())


    def get_state_city_choice(self, obj):
        return list(STATE_CITY_CHOICE.values())

