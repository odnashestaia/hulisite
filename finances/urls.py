from django.urls import path
from .views import fin_list, fin_add, fin_delete

app_name = 'fin'
urlpatterns = [
    path('', fin_list, name='list'),
    path('create', fin_add, name='create'),
    path('delete/<int:pk>', fin_delete, name='delete'),
]