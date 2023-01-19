from django.urls import path
from .views import *

app_name = 'myapp'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', about, name='about'),
    path('add_item/', AddItem.as_view(), name='add_item'),
    path('contact/', Contacts.as_view(), name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    # path('logout/', LogoutUser.as_view(), name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('item/<slug:slug>/', ItemDetail.as_view(), name='item_detail'),
    path('category/<int:pk>/', CategoryDetail.as_view(), name='category_detail'),


]

