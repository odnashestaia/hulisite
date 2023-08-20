import datetime
from django.contrib.auth.models import User
from django.db import models


class Todo(models.Model):
    text = models.CharField(max_length=400, verbose_name='Text task')
    is_complete = models.BooleanField(default=False, verbose_name='Status')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_for_do = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.text
