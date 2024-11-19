from .models import Organization
from rest_framework import serializers
from address.serializers import AddressSerializer
from address.defaults import AREA_CHOICES, ADDRESS_TYPE, STATE_CITY_CHOICE

class OrganizationSerializer(serializers.ModelSerializer):
    address_base = AddressSerializer(read_only=True, source="address")


    class Meta:
        model = Organization
        fields = ['id', 'name', 'phone', 'address', 'address_base', 'area', 'description']


class StatusChoicesSerializer(serializers.Serializer):
    area_choices = serializers.SerializerMethodField()
    address_type = serializers.SerializerMethodField()
    state_city_choice = serializers.SerializerMethodField()


    def get_area_choices(self, obj):
        return [{'id': key, 'title': value} for key, value in AREA_CHOICES.items()]


    def get_address_type(self, obj):
        return [{'id': key, 'title': value} for key, value in ADDRESS_TYPE.items()]


    def get_state_city_choice(self, obj):
        return [{'id': key, 'title': value} for key, value in STATE_CITY_CHOICE.items()]
