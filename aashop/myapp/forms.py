from django import forms
from .models import *

class ItemForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'size': 50}))
    text = forms.CharField(widget=forms.Textarea)
    price = forms.IntegerField(min_value=0)
    is_piblished = forms.BooleanField()
    slug = forms.SlugField()
    cat = forms.ModelChoiceField(queryset=Category.objects, widget=forms.RadioSelect)