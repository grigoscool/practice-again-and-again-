from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import *

menu = [
    {'title': 'о сайте', 'url': 'about'},
    {'title': 'добавть товар', 'url': 'add_item'},
    {'title': 'обратная связь', 'url': 'contact'},
    {'title': 'Войти', 'url': 'login'}
]


def show_home(request):
    item = Item.objects.all()
    cat = Category.objects.all()
    context = {
        'item': item,
        'menu': menu,
        'categories': cat,
    }
    return render(request, 'myapp/home.html', context)


def about(request):
    return render(request, 'myapp/about.html', {'menu': menu})


def show_contact(request):
    return render(request, 'myapp/contact.html', {'menu': menu})


def add_item(request):
    return render(request, 'myapp/add_item.html', {'menu': menu})


def login(request):
    return render(request, 'myapp/login.html', {'menu': menu})


def show_item_detail(request, pk):
    item = Item.objects.get(pk=pk)
    context = {
        'item': item,
        'menu': menu,
    }
    return render(request, 'myapp/item_detail.html', context)
