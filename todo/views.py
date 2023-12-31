import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .models import Todo


def todo_list(request):
    if request.user.is_authenticated:
        todos = Todo.objects.filter(author=request.user).order_by('-id').order_by('is_complete')
    else:
        todos = [{'text': 'Test text', 'is_complete': False, 'date_for_do': '2023.12.23'}]
    return render(request, 'todo/index_todo.html', {'todos': todos})


@require_http_methods(['GET', 'POST'])
def edit_task(request, pk):
    todo = Todo.objects.get(pk=pk)

    if request.method == 'POST':
        todo.text = request.POST.get('title')
        todo.save()

        return render(request, 'todo/list_todo.html', {'todo': todo})
    return render(request, 'todo/edit.html', {'todo': todo})


@require_http_methods(['POST'])
def add_todo(request):
    todo = None
    text = request.POST.get('title')

    if text:
        todo = Todo.objects.create(text=text, author=request.user)

    return render(request, 'todo/list_todo.html', {'todo': todo})


@require_http_methods(['PUT'])
def update_task(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.is_complete = not todo.is_complete
    todo.save()

    return render(request, 'todo/list_todo.html', {'todo': todo})


@require_http_methods(['DELETE'])
def delete_task(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()

    return HttpResponse()
