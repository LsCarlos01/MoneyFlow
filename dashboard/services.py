from datetime import date
import calendar
from django.db.models import Sum
from transacoes.models import Transacoes
from django.db.models.functions import TruncMonth

def transacoes_no_mes(tipo=None):
    hoje = date.today()
    primeiro_dia = hoje.replace(day=1)
    ultimo_dia = date(
        hoje.year,
        hoje.month,
        calendar.monthrange(hoje.year, hoje.month)[1]
    )

    qs = Transacoes.objects.filter(
        data__gte=primeiro_dia,
        data__lte=ultimo_dia
    )

    if tipo:
        qs = qs.filter(categoria__tipo=tipo)

    return qs

def total_gasto_no_mes():
      return (
        transacoes_no_mes(tipo="saida")
        .aggregate(total=Sum("valor"))["total"] or 0
    )
def total_gasto_por_categoria():
      return (
        transacoes_no_mes(tipo="saida")
        .values("categoria__nome")
        .annotate(total=Sum("valor"))
        .order_by("-total")
    )

def evolucao_mensal():
    dados = (
        Transacoes.objects
        .filter(categoria__tipo="saida")
        .annotate(mes=TruncMonth("data"))
        .values("mes")
        .annotate(total=Sum("valor"))
        .order_by("mes")
    )

    meses = [item["mes"].strftime("%Y-%m") for item in dados]
    totais = [float(item["total"]) for item in dados]

    return meses, totais

def total_entrada_no_mes():
    return (
        transacoes_no_mes(tipo="entrada")
        .aggregate(total=Sum("valor"))["total"] or 0
    )


def saldo_do_mes():
    return total_entrada_no_mes() - total_gasto_no_mes()