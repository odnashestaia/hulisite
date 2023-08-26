from django.urls import path
from .views import todo_list, add_todo, update_task, delete_task, edit_task

app_name = 'todo'
urlpatterns = [
    path('', todo_list, name='list'),
    path('add-todo', add_todo, name='add'),
    path('update/<int:pk>', update_task, name='update'),
    path('delete/<int:pk>', delete_task, name='delete'),
    path('edit/<int:pk>', edit_task, name='edit'),

]
