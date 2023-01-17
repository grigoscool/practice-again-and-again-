from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', about, name='about'),
    path('add_item', add_item, name='add_item'),
    path('contact', show_contact, name='contact'),
    path('login', login, name='login'),
    path('item/<slug:slug>/', show_item_detail, name='item_detail'),
    path('category/<int:pk>/', show_category_detail, name='category_detail'),

]

