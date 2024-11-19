from django_filters import rest_framework as filters
from .models import Pessoa


class PessoaFilter(filters.FilterSet):
    nome = filters.CharFilter(field_name='nome', lookup_expr='icontains')
    idade = filters.CharFilter(field_name='idade', lookup_expr='icontains')


    class Meta:
        model = Pessoa
        fields = ['nome', 'idade']