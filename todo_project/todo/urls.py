"""todo_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *

# each path is assigned with a view
urlpatterns = [
    path('', mainView, name="home"),
    path('add_Todo/', addTodo, name="add_Todo"),
    path('update_Todo/<int:pk>/', updateTodo, name="update_Todo"),
    path('delete_Todo/<int:pk>/', deleteTodo, name="delete_Todo"),
    path('login/', loginView, name="login"),
    path('logout/', logoutView, name="logout"),
    path('register/', registerView, name="register"),
    # we use a parameter by using '< >'
]
