from django.shortcuts import render
from .services import *

def dashboard(request):
    total_gasto_mes = total_gasto_no_mes()
    dados_categorias = total_gasto_por_categoria()
    meses, totais = evolucao_mensal()


    categorias = [item["categoria__nome"] for item in dados_categorias]
    valores = [float(item["total"]) for item in dados_categorias]


    context = {
        'meses': meses,
        'totais': totais,
        'total_gasto_mes': total_gasto_mes,
        'categorias': categorias,
        'valores': valores,
    }

    return render(request, 'dashboard/dashboard.html', context)
