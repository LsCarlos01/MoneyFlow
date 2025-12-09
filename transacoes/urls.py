from django.urls import path
from .views import listar_trasacoes, adicionar_transacao

urlpatterns = [
    path('', listar_trasacoes, name='listar_transacoes'),
    path('cadastrar/', adicionar_transacao, name='adicionar_transacao'),
]
