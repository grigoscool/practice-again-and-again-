from django.urls import path, include, re_path
from rest_framework import routers

from myapp.views import *

app_name = 'myapp'

routers = routers.SimpleRouter()
routers.register(r'item', ItemApiViewSet)
print(routers.urls)
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', about, name='about'),
    path('add_item/', AddItem.as_view(), name='add_item'),
    path('contact/', Contacts.as_view(), name='contact'),
    path('item/<slug:slug>/', cache_page(60 * 1)(ItemDetail.as_view()), name='item_detail'),
    path('category/<int:pk>/', CategoryDetail.as_view(), name='category_detail'),
    path('search/', SearchResult.as_view(), name='search'),
    path('api/v1/', include(routers.urls)),
    path('api/v1/auth_dj/', include('djoser.urls')),
    re_path(r'^auth_dj/', include('djoser.urls.authtoken')),
]
