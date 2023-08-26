from django.contrib import admin

from .models import Account, Transaction, Categories


admin.site.register(Categories)


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['user', 'balance']


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['description', 'amount', 'transaction_date']
