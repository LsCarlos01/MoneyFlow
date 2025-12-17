from .models import Categoria
from .forms import CategoriaForm
from django.shortcuts import render, redirect, get_object_or_404

def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categoria/listar_categorias.html', {'categorias': categorias})


def cadastrar_categorias(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categoria:listar_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'categoria/cadastrar_categoria.html', {'form': form})

def categoria_delete(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)

    if request.method == "POST":
        categoria.delete()

    return redirect('categoria:listar_categorias')

def categoria_edit(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('categoria:listar_categorias')
    else:
        form = CategoriaForm(instance=categoria)
        
    return render(request, 'categoria/editar_categoria.html', {'form': form, 'categoria': categoria})


# Create your views here.
