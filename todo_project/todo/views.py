from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem
# Create your views here.

def todoView(request):
    context = {
        'all_items': TodoItem.objects.all()
    }
    return render(request, 'todo/todo.html', 
        context)

def addTodo(request):
    if request.method == 'POST':
        new_item = TodoItem(content = request.POST['content'])
        new_item.save()
    return HttpResponseRedirect('http://127.0.0.1:8000')

def deleteTodo(request, todo_id):
    if request.method == 'POST':
        deleted_todo = TodoItem.objects.get(id=todo_id)
        deleted_todo.delete()
        return HttpResponseRedirect('http://127.0.0.1:8000')
