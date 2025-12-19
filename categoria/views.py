from .models import Categoria
from .forms import CategoriaForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required
def listar_categorias(request):
    categorias = Categoria.objects.filter(user=request.user)
    return render(request, 'categoria/listar_categorias.html', {'categorias': categorias})

@login_required
def cadastrar_categorias(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            categoria=form.save(commit=False)
            categoria.user = request.user
            categoria.save() 
            return redirect('categoria:listar_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'categoria/cadastrar_categoria.html', {'form': form})

@login_required
def categoria_delete(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk, user=request.user)

    if request.method == "POST":
        categoria.delete()

    return redirect('categoria:listar_categorias')

@login_required
def categoria_edit(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk, user=request.user)
    
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('categoria:listar_categorias')
    else:
        form = CategoriaForm(instance=categoria)
        
    return render(request, 'categoria/editar_categoria.html', {'form': form, 'categoria': categoria})


# Create your views here.
