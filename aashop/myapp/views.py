from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from rest_framework import generics, viewsets
from django.views.decorators.cache import cache_page
from django.views.generic import ListView, TemplateView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *
from .forms import ItemForm
from .serializer import ItemSerializer
from .utils import DataMixin


class Home(DataMixin, ListView):
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
        mix_cont = self.get_user_context(title='Home')
        return context | mix_cont

    # создаем запросдля отображения в шаблоне
    def get_queryset(self):
        return Item.objects.filter(is_piblished=True).select_related('cat')


@cache_page(60 * 1)
def about(request):
    return render(request, 'myapp/about.html')


class Contacts(DataMixin, TemplateView):
    template_name = 'myapp/contact.html'

    def get_context_data(self, **kwargs):
        context = super(Contacts, self).get_context_data()
        mix_cont = self.get_user_context(title='Contact')
        return context | mix_cont


class AddItem(LoginRequiredMixin, DataMixin, CreateView):
    form_class = ItemForm
    template_name = 'myapp/add_item.html'
    context_object_name = 'form'
    login_url = '/login/'

    def get_context_data(self, **kwargs):
        context = super(AddItem, self).get_context_data()
        mix_cont = self.get_user_context(title='ADD item')
        return context | mix_cont

class ItemDetail(DataMixin, DetailView):
    model = Item
    context_object_name = 'item'
    template_name = 'myapp/item_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ItemDetail, self).get_context_data()
        mix_cont = self.get_user_context(title=self.kwargs['slug'])
        return context | mix_cont


class CategoryDetail(DataMixin, ListView):
    model = Category
    template_name = 'myapp/category_detail.html'
    context_object_name = 'items'
    # атрибут из датамиксин
    allow_empty = False

    def get_queryset(self):
        # через кваргс можем получить значение из словоря ЗАПРОСА урла
        return Item.objects.filter(cat_id=self.kwargs['pk'], is_piblished=True).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        mix_cont = self.get_user_context(title='Category - ' + str(context['items'][0].cat))
        return context | mix_cont


class SearchResult(DataMixin, ListView):
    model = Item
    template_name = 'myapp/search_result.html'
    context_object_name = 'item'

    def get_queryset(self):
        search_item = self.request.GET.get('search')
        item = Item.objects.filter(name__icontains=search_item)
        return item


class ItemApiViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

