from django.urls import path

from myapp.views import *

app_name = 'myapp'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', about, name='about'),
    path('add_item/', AddItem.as_view(), name='add_item'),
    path('contact/', Contacts.as_view(), name='contact'),
    path('item/<slug:slug>/', cache_page(60 * 1)(ItemDetail.as_view()), name='item_detail'),
    path('category/<int:pk>/', CategoryDetail.as_view(), name='category_detail'),
    path('search/', SearchResult.as_view(), name='search'),
    path('api/v1/item/', ItemApiView.as_view()),
]
