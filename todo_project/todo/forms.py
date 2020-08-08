from django.forms import ModelForm
from .models import *

class TodoForm(ModelForm):
    class Meta:
        model = TodoItem
        fields = '__all__'