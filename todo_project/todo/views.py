from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def mainView(request):
    context = {
        'todo_items': TodoItem.objects.all()
    }
    return render(request, 'todo/main.html', context)

def logoutView(request):
    logout(request) 
    return redirect('login')

def loginView(request):
    if request.user.is_authenticated:
        return redirect('home')
    else: 
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or Password is incorrect.')
        context = {

        }
        return render(request, 'todo/login.html', context)

def registerView(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:     
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Welcome, ' + user)
                return redirect('login')

        context = {
            'form': form
        }
        return render(request, 'todo/register.html', context)

@login_required(login_url='login')
def addTodo(request):
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form': form}
    return render(request, 'todo/create.html', context)

@login_required(login_url='login')
def updateTodo(request, pk):
    item = TodoItem.objects.get(id=pk)
    form = TodoForm(instance=item)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form': form}
    return render(request, 'todo/update.html', context)

@login_required(login_url='login')
def deleteTodo(request, pk):
    item = TodoItem.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    
    context = {'item': item }
    return render(request, 'todo/delete.html', context)
