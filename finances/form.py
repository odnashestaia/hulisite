from django.forms import ModelForm

from finances.models import Transaction


class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['description', 'amount', 'transaction_date', 'categories']
