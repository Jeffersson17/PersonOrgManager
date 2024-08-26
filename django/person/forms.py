from django import forms
from .models import Pessoa


class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome', 'idade']


    def clean(self):
        cleaned_data = super().clean()
        nome = cleaned_data.get('nome')
        idade = cleaned_data.get('idade')

        if nome and len(nome) <= 3:
            self.add_error('nome', 'O campo nome deve conter mais de 3 letras.')

        if idade is not None and idade <= 18:
            self.add_error('idade', 'O campo idade deve ser maior que 18.')

        return cleaned_data
