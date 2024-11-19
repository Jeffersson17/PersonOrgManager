from django_filters import rest_framework as filters
from .models import Organization


class OrganizationFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    address = filters.CharFilter(field_name='address__id', lookup_expr='icontains')


    class Meta:
        model = Organization
        fields = ['name', 'address']
