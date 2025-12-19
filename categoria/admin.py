from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Categoria

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'user')
    search_fields = ('nome',)
    list_filter = ('user',)