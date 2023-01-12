from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import *

menu = ['главная', 'о сайте']


def show_home(request):
    item = Item.objects.all()
    return render(request, 'myapp/home.html', {'item': item, 'menu': menu})



def about(request):
    return render(request, 'myapp/about.html', {'menu': menu})
