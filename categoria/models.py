from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    tipo = models.CharField(
        max_length=7,
        choices=[
            ('entrada', 'Entrada'),
            ('saida', 'Saída'),
        ]
    )

    def __str__(self):
        return f"{self.nome} ({self.tipo})"