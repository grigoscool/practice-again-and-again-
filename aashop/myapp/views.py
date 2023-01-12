from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404


def show_home(request):
    return HttpResponse('hello my friend')

def show_cat(request, slug):
    if slug == 'ff':
        return redirect('home')
    return HttpResponse(f"{slug} you now")


