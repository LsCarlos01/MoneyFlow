from django.db import models
from categoria.models import Categoria

# Create your models here.
class Transacoes(models.Model):
    valor= models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL,
    null=True,
    blank=True
    )
    data= models.DateField()
    
    def __str__(self):
        return f"{self.valor} ({self.categoria})" 