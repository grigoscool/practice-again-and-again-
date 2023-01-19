from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *
from .forms import ItemForm, RegistrationForm
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
        return Item.objects.filter(is_piblished=True)


@login_required(login_url='/login/')
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
        mix_cont = self.get_user_context(title=Item.objects.get(slug=self.kwargs['slug']))
        return context | mix_cont


class CategoryDetail(DataMixin, ListView):
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
        mix_cont = self.get_user_context(title='Category - ' + str(context['items'][0].cat))
        return context | mix_cont


class RegisterUser(DataMixin, CreateView):
    form_class = RegistrationForm
    template_name = 'myapp/register.html'
    context_object_name = 'form'
    success_url = reverse_lazy('myapp:login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('myapp:home')


class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'myapp/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        mix_cont = self.get_user_context(title='авторизация')
        return context | mix_cont


def logout_user(request):
    logout(request)
    return redirect('myapp:login')
