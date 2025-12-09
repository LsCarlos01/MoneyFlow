from django.shortcuts import render, redirect
from .models import Categoria
from .forms import CategoriaForm


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


# Create your views here.
