from django.urls import path
from .views import show_home, show_cat

urlpatterns = [
    path('', show_home, name='home'),
    path('cat/<slug:slug>/', show_cat, name='cat_list'),
]

