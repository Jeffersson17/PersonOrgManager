from django import forms
from .models import City, Address

class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name', 'state']


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        field = ['address', 'address_type', 'city', 'cep', 'number', 'complement',]