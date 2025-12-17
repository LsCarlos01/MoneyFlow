from django import forms
from .models import Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome', 'tipo', 'descricao']
        widgets = {
            'descricao': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Ex: gastos com mercado, lanches e refeições'
            })
        }