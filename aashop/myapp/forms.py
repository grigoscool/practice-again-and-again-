from django import forms
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


