from django.shortcuts import render, redirect
from .models import Transacoes
from .forms import TransacoesForm


def listar_trasacoes(request):
    transacoes = Transacoes.objects.all()
    return render(request, 'transacoes/listar_transacoes.html', {'transacoes': transacoes})

def adicionar_transacao(request):  
    if request.method == 'POST':
        form= TransacoesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_transacoes')
    else:
        form = TransacoesForm()
    return render(request, 'transacoes/cadastrar_transacoes.html', {'form': form})
    