from django.db.models import Count
from django.shortcuts import render
from .models import Transaction
from django.views.decorators.http import require_http_methods


def fin_list(request):
    fin = Transaction.objects.all().filter(account__user=request.user)

    return render(request, 'fin/fin_list.html', {'finances': fin})


@require_http_methods(['POST'])
def fin_add(request):
    tran = None
    des = request.POST.get('description')
