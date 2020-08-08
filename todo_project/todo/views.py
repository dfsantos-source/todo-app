from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *
# Create your views here.

def mainView(request):
    context = {
        'todo_items': TodoItem.objects.all()
    }
    return render(request, 'todo/main.html', 
        context)

def addTodo(request):
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form': form}
    return render(request, 'todo/todo_form.html', context)

def updateTodo(request, pk):
    item = TodoItem.objects.get(id=pk)
    form = TodoForm(instance=item)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form': form}
    return render(request, 'todo/todo_form.html', context)


def deleteTodo(request, todo_id):
    if request.method == 'POST':
        deleted_todo = TodoItem.objects.get(id=todo_id)
        deleted_todo.delete()
        return HttpResponseRedirect('http://127.0.0.1:8000')
