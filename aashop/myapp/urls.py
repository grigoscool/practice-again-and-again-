from django.urls import path
from .views import *

urlpatterns = [
    path('', show_home, name='home'),
    path('about/', about, name='about')
]

