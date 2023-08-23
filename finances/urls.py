from django.urls import path
from .views import fin_list

urlpatterns = [
    path('', fin_list, name='fin_list'),
]