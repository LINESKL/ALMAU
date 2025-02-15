from django.shortcuts import render, redirect
from django.http import Http404
from .models import Todo
from .forms import TodoForm


def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todos/todo_list.html', {'todos': todos})


def todo_detail(request, id):
    try:
        todo = Todo.objects.get(id=id)
    except Todo.DoesNotExist:
        raise Http404("Todo not found")
    return render(request, 'todos/todo_detail.html', {'todo': todo})


def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todos/todo_form.html', {'form': form})


def todo_edit(request, id):
    try:
        todo = Todo.objects.get(id=id)
    except Todo.DoesNotExist:
        raise Http404("Todo not found")

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todos/todo_form.html', {'form': form, 'is_edit': True})


def todo_delete(request, id):
    try:
        todo = Todo.objects.get(id=id)
    except Todo.DoesNotExist:
        raise Http404("Todo not found")

    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')
    return redirect('todo_list')