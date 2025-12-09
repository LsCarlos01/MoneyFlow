from django.urls import path
from .views import listar_categorias, cadastrar_categorias

app_name = 'categoria'



urlpatterns = [
    path('', listar_categorias, name='listar_categorias'),
    path('cadastrar/', cadastrar_categorias, name='cadastrar_categorias'),

]
