from django.shortcuts import render
from .services import *
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    user = request.user

    total_gasto_mes = total_gasto_no_mes(user)
    total_entrada_mes = total_entrada_no_mes(user)
    saldo_mes = saldo_do_mes(user)

    dados_categorias = total_gasto_por_categoria(user)
    meses, totais = evolucao_mensal(user)

    categorias = [item["categoria__nome"] for item in dados_categorias]
    valores = [float(item["total"]) for item in dados_categorias]

    context = {
        'meses': meses,
        'totais': totais,
        'total_gasto_mes': total_gasto_mes,
        'total_entrada_mes': total_entrada_mes,
        'saldo_mes': saldo_mes,
        'categorias': categorias,
        'valores': valores,
    }

    return render(request, 'dashboard/dashboard.html', context)
