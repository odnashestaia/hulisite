import datetime

from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render
from .models import Transaction, Categories, Account
from django.views.decorators.http import require_http_methods


def fin_list(request):
    fin = Transaction.objects.all().filter(account__user=request.user).order_by('-id')
    categories = Categories.objects.all()
    acc = Account.objects.get(user=request.user)
    return render(request, 'fin/index.html',
                  {'finances': fin, 'categories': categories, 'account': acc})


@require_http_methods(['POST'])
def fin_add(request):
    tran = None
    des = request.POST.get('des')
    acc = Account.objects.get(user=request.user)
    if des:
        tran = Transaction.objects.create(description=des, account=Account.objects.get(user=request.user),
                                          amount=request.POST.get('amount'),
                                          transaction_date=request.POST.get('transaction_date'),
                                          categories_id=request.POST.get('categories'))
        acc.balance += int(request.POST.get('amount'))
        acc.save()
    tran_all = Transaction.objects.all().filter(account__user=request.user).order_by('-id')
    return render(request, 'fin/list.html', {'finances': tran_all, 'account': acc})


@require_http_methods(['DELETE'])
def fin_delete(request, pk):
    tran = Transaction.objects.get(pk=pk)
    acc = Account.objects.get(user=request.user)
    if int(tran.amount) > 0:
        acc.balance -= int(tran.amount)
    else:
        acc.balance -= int(tran.amount)
    acc.save()
    tran.delete()
    return HttpResponse()
