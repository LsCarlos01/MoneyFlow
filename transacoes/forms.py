from django import forms
from .models import Transacoes

class TransacoesForm(forms.ModelForm):
    class Meta:
        model = Transacoes
        fields = ['valor', 'categoria', 'data']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
        }