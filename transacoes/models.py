from django.db import models
from categoria.models import Categoria
from django.contrib.auth.models import User

# Create your models here.
class Transacoes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='transacoes')
    valor= models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL,
    null=True,
    blank=True
    )
    data= models.DateField()

    def __str__(self):
        return f"{self.valor} ({self.categoria})" 