import datetime

from django.contrib.auth.models import User
from django.db import models


class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        if self.user.get_full_name() == '':
            return self.user.get_username()
        return self.user.get_full_name()


class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=100)
    transaction_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f'{self.description} - {self.amount}'

