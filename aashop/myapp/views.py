from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from .models import *
from .forms import ItemForm

menu = [
    {'title': 'о сайте', 'url': 'about'},
    {'title': 'добавть товар', 'url': 'add_item'},
    {'title': 'обратная связь', 'url': 'contact'},
    {'title': 'Войти', 'url': 'login'}
]


def show_home(request):
    item = Item.objects.all()
    context = {
        'item': item,
        'menu': menu,
    }
    return render(request, 'myapp/home.html', context)


def about(request):
    return render(request, 'myapp/about.html', {'menu': menu})


def show_contact(request):
    return render(request, 'myapp/contact.html', {'menu': menu})


def add_item(request):
    if request.method == 'POST':
        form = ItemForm(data=request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        return render(request, 'myapp/add_item.html', {'menu': menu, 'form': form})
    else:
        form = ItemForm()
        return render(request, 'myapp/add_item.html', {'menu': menu, 'form': form})

def login(request):
    return render(request, 'myapp/login.html', {'menu': menu})


def show_item_detail(request, slug):
    item = get_object_or_404(Item, slug=slug)
    context = {
        'item': item,
        'menu': menu,
    }
    return render(request, 'myapp/item_detail.html', context)


def show_category_detail(request, pk):
    items = Item.objects.filter(cat_id=pk)
    context = {
        'items': items,
        'menu': menu,
    }
    if not items:
        raise Http404
    return render(request, 'myapp/category_detail.html', context)
