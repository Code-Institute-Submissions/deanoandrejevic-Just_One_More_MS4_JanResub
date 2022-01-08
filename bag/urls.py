from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<item_id>', views.add_to_basket, name='add_to_basket')
] 
