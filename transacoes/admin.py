from django.contrib import admin
from .models import Transacoes

@admin.register(Transacoes)
class TransacaoAdmin(admin.ModelAdmin):
    list_display = ('valor', 'user', 'categoria')
    list_filter = ('user', 'categoria')