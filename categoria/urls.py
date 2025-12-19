from django.urls import path
from .views import *

app_name = 'categoria'

urlpatterns = [
    path('', listar_categorias, name='listar_categorias'),
    path('cadastrar/', cadastrar_categorias, name='cadastrar_categorias'),
    path('categoria/<int:pk>/deletar', categoria_delete, name='categoria_delete'),
    path('categoria/<int:pk>/editar', categoria_edit, name='categoria_edit'),
]
