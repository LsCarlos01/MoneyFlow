from django.shortcuts import render, redirect, get_object_or_404
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

def transacoes_delete(request, pk):
    transacao = get_object_or_404(Transacoes, pk=pk)
    if request.method == 'POST':
        transacao.delete()
        return redirect('listar_transacoes')
    return redirect('listar_transacoes')

    