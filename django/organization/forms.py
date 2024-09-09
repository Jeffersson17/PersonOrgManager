from django import forms
from .models import Organization

class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['phone', 'address', 'area']


    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('nome')
        phone = cleaned_data.get('phone')
        address = cleaned_data.get('address')
        area = cleaned_data.get('area')
        description = cleaned_data.get('description')

        if phone:
            if not phone.isdigit():
                self.add_error('phone', 'O telefone deve conter apenas dígitos.')
            elif len(phone) < 10:
                self.add_error('phone', 'O telefone deve ter no mínimo 10 dígitos.')

        if len(phone) < 10:
            self.add_error('phone', 'O telefone deve ter no mínimo 10 digitos.')

        if not area:
            self.add_error('area', 'A área é obrigatória.')

        if not address:
            self.add_error('address', 'O endereço é obrigatório.')

        return cleaned_data
