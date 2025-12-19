from django.shortcuts import render, redirect, get_object_or_404
from .models import Transacoes
from .forms import TransacoesForm
from categoria.models import Categoria
from django.contrib.auth.decorators import login_required

@login_required
def listar_trasacoes(request):
    transacoes = Transacoes.objects.filter(user=request.user)
    return render(request, 'transacoes/listar_transacoes.html', {'transacoes': transacoes})

@login_required
def adicionar_transacao(request):
    categoria_id= request.GET.get('categoria')

    categoria= None
    if categoria_id:
        categoria= Categoria.objects.filter(id=categoria_id, user=request.user).first()

    if request.method == 'POST':
        form= TransacoesForm(request.POST)
        if form.is_valid():
            transacao= form.save(commit=False)
            transacao.user= request.user
            if categoria:
                transacao.categoria=categoria
            transacao.save()
            return redirect('listar_transacoes')
    else:
        form = TransacoesForm(initial={'categoria': categoria})

    return render(request, 'transacoes/cadastrar_transacoes.html', {'form': form , 'categoria_fixa': categoria})

@login_required
def transacoes_delete(request, pk):
    transacao = get_object_or_404(Transacoes, pk=pk, user=request.user)
    if request.method == 'POST':
        transacao.delete()
        return redirect('listar_transacoes')
    return redirect('listar_transacoes')

@login_required
def edit_transacao(request, pk):
    transacao = get_object_or_404(Transacoes, pk=pk, user=request.user)
    categoria_fixa = transacao.categoria
    if request.method == 'POST':
        form = TransacoesForm(request.POST, instance=transacao)
        if form.is_valid():
            transacao_editada= form.save(commit=False)
            transacao_editada.categoria= categoria_fixa
            transacao_editada.save()
            return redirect('listar_transacoes')
    else:
        form = TransacoesForm(instance=transacao)
    return render(request, 'transacoes/edit_transacoes.html', {'form': form, 'categoria_fixa': categoria_fixa})


