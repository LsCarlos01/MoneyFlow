from django.urls import path
from .views import *

urlpatterns = [
    path('', listar_trasacoes, name='listar_transacoes'),
    path('cadastrar/', adicionar_transacao, name='adicionar_transacao'),
    path('transacoes/<int:pk>/delete', transacoes_delete, name='transacoes_delete'),
    path('transacoes/<int:pk>/edit', edit_transacao, name='edit_transacao')
]
