from datetime import date
import calendar
from django.db.models import Sum
from transacoes.models import Transacoes
from django.db.models.functions import TruncMonth

def transacoes_no_mes(user ,tipo=None):
    hoje = date.today()
    primeiro_dia = hoje.replace(day=1)
    ultimo_dia = date(
        hoje.year,
        hoje.month,
        calendar.monthrange(hoje.year, hoje.month)[1]
    )

    qs = Transacoes.objects.filter(user=user,
        data__gte=primeiro_dia,
        data__lte=ultimo_dia
    )

    if tipo:
        qs = qs.filter(categoria__tipo=tipo)

    return qs

def total_gasto_no_mes(user):
      return (
        transacoes_no_mes(user, tipo="saida")
        .aggregate(total=Sum("valor"))["total"] or 0
    )
def total_gasto_por_categoria(user):
      return (
        transacoes_no_mes(user, tipo="saida")
        .values("categoria__nome")
        .annotate(total=Sum("valor"))
        .order_by("-total")
    )

def evolucao_mensal(user):
    qs = (
        Transacoes.objects
        .filter(user=user, categoria__tipo="saida")
        .annotate(mes=TruncMonth("data"))
        .values("mes")
        .annotate(total=Sum("valor"))
        .order_by("mes")
    )

    meses = []
    totais = []

    for item in qs:
        meses.append(item["mes"].strftime("%Y-%m"))
        totais.append(float(item["total"]))

    return meses, totais

def total_entrada_no_mes(user):
    return (
        transacoes_no_mes(user, tipo="entrada")
        .aggregate(total=Sum("valor"))["total"] or 0
    )


def saldo_do_mes(user):
    return total_entrada_no_mes(user) - total_gasto_no_mes(user)