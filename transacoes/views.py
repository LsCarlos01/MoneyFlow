from django.shortcuts import render, redirect, get_object_or_404
from .models import Transacoes
from .forms import TransacoesForm
from categoria.models import Categoria


def listar_trasacoes(request):
    transacoes = Transacoes.objects.all()
    return render(request, 'transacoes/listar_transacoes.html', {'transacoes': transacoes})

def adicionar_transacao(request):
    categoria_id= request.GET.get('categoria')
    if categoria_id:
        categoria= Categoria.objects.filter(id=categoria_id).first()
    else:
        categoria= None

    if request.method == 'POST':
        form= TransacoesForm(request.POST)
        if form.is_valid():
            transacao= form.save()
            if categoria:
                transacao.categoria=categoria
            transacao.save()
            return redirect('listar_transacoes')
    else:
        form = TransacoesForm(initial={'categoria': categoria})

    return render(request, 'transacoes/cadastrar_transacoes.html', {'form': form , 'categoria_fixa': categoria})

def transacoes_delete(request, pk):
    transacao = get_object_or_404(Transacoes, pk=pk)
    if request.method == 'POST':
        transacao.delete()
        return redirect('listar_transacoes')
    return redirect('listar_transacoes')

def edit_transacao(request, pk):
    transacao = get_object_or_404(Transacoes, pk=pk)
    categoria_fixa = transacao.categoria
    if request.method == 'POST':
        form = TransacoesForm(request.POST, instance=transacao)
        if form.is_valid:
            transacao_editada= form.save(commit=False)
            transacao_editada.categoria= categoria_fixa
            transacao_editada.save()
            return redirect('listar_transacoes')
    else:
        form = TransacoesForm(instance=transacao)
    return render(request, 'transacoes/edit_transacoes.html', {'form': form, 'categoria_fixa': categoria_fixa})


