from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from myapp.forms import RegistrationForm
from myapp.utils import DataMixin


class RegisterUser(DataMixin, CreateView):
    form_class = RegistrationForm
    template_name = 'authentication/register.html'
    context_object_name = 'form'
    success_url = reverse_lazy('auth:login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('auth:home')


class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'authentication/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        mix_cont = self.get_user_context(title='авторизация')
        return context | mix_cont


def logout_user(request):
    logout(request)
    return redirect('auth:login')
