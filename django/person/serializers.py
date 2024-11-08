from .models import Pessoa
from rest_framework import serializers


class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = ['id', 'nome', 'idade']


    def validate_idade(self, value):
        if value < 18:
            raise serializers.ValidationError('A idade não pode ser menor que 18.')
        return value


    def validate_nome(self, value):
        if len(value) <= 3:
            raise serializers.ValidationError('O nome deve conter mais de 3 caracteres.')
        return value
