from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='categorias')
    nome = models.CharField(max_length=100)
    tipo = models.CharField(
        max_length=7,
        choices=[
            ('entrada', 'Entrada'),
            ('saida', 'Saída'),
        ]
    )
    descricao = models.TextField(blank=True)
   
    class Meta:
        unique_together = ('user', 'nome')
        

    def __str__(self):
        return f"{self.nome} ({self.tipo})"