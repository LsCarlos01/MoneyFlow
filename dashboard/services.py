from datetime import date
import calendar
from django.db.models import Sum
from transacoes.models import Transacoes
from django.db.models.functions import TruncMonth

def transacoes_no_mes():
    hoje = date.today()
    primeiro_dia= hoje.replace(day=1)

    ultimo_dia= date (
        hoje.year,
        hoje.month,
        calendar.monthrange(hoje.year, hoje.month)[1]
    )

    return Transacoes.objects.filter(
        data__gte=primeiro_dia,
        data__lte=ultimo_dia
    )
    

def total_gasto_no_mes():
    transacoes_mes= transacoes_no_mes()
    total= transacoes_mes.aggregate(total=Sum("valor"))["total"] or 0

    return total

def total_gasto_por_categoria():
    transacoes_mes= transacoes_no_mes()
    return (
        transacoes_mes
        .values("categoria__nome")
        .annotate(total=Sum("valor"))
        .order_by("-total")
    )

def evolucao_mensal():
    dados = (
        Transacoes.objects
        .annotate(mes=TruncMonth("data"))
        .values("mes")
        .annotate(total=Sum("valor"))
        .order_by("mes")
    )
    
    meses = [item["mes"].strftime("%Y-%m") for item in dados]
    totais = [float(item["total"]) for item in dados]

    return meses, totais