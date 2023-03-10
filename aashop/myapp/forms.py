from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import TextInput

from .models import *
from django.core import validators


class ItemForm(forms.ModelForm):
    # для переопредения атрибутов
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'no cat'

    # наследование от модели всех полей
    class Meta:
        model = Item
        fields = ['name', 'slug', 'price', 'is_piblished', 'text', 'photo', 'cat']
        # переопределения виджетов от модели к форме
        widgets = {
            'name': TextInput(attrs={'size': 50})
        }

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

