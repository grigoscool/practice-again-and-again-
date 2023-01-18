from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.views.generic import ListView, TemplateView, DetailView, CreateView

from .models import *
from .forms import ItemForm

menu = [
    {'title': 'о сайте', 'url': 'about'},
    {'title': 'добавть товар', 'url': 'add_item'},
    {'title': 'обратная связь', 'url': 'contact'},
    {'title': 'Войти', 'url': 'login'}
]


class Home(ListView):
    model = Item
    # меняем стандартную директорию на уже имеющуюся
    template_name = 'myapp/home.html'
    # Класс вьюхи отправляет object_list, мы же меняемна items
    context_object_name = 'items'
    # так можно передать статические данные без переменных
    extra_context = {'title': 'Home'}
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        # добавляем данные во вьюху
        context['menu'] = menu
        return context

    # создаем запросдля отображения в шаблоне
    def get_queryset(self):
        return Item.objects.filter(is_piblished=True)


class About(TemplateView):
    template_name = 'myapp/about.html'

    def get_context_data(self, **kwargs):
        context = super(About, self).get_context_data()
        context['menu'] = menu
        context['title'] = 'about'
        return context


def show_contact(request):
    return render(request, 'myapp/contact.html', {'menu': menu})


class AddItem(CreateView):
    form_class = ItemForm
    template_name = 'myapp/add_item.html'
    context_object_name = 'form'

    def get_context_data(self, **kwargs):
        context = super(AddItem, self).get_context_data()
        context['menu'] = menu
        context['title'] = 'ADD item'
        return context


def login(request):
    return render(request, 'myapp/login.html', {'menu': menu})


class ItemDetail(DetailView):
    model = Item
    context_object_name = 'item'
    template_name = 'myapp/item_detail.html'


class CategoryDetail(ListView):
    model = Category
    template_name = 'myapp/category_detail.html'
    context_object_name = 'items'
    # атрибут из датамиксин
    allow_empty = False

    def get_queryset(self):
        # через кваргс можем получить значение из словоря ЗАПРОСА урла
        return Item.objects.filter(cat_id=self.kwargs['pk'], is_piblished=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Category - ' + str(context['items'][0].cat)
        context['menu'] = menu
        return context
