from django.urls import path
from .views import *

urlpatterns = [
    path('', show_home, name='home'),
    path('about/', about, name='about'),
    path('add_item', add_item, name='add_item'),
    path('contact', show_contact, name='contact'),
    path('login', login, name='login'),
    path('item/<int:pk>/', show_item_detail, name='item_detail'),

]

