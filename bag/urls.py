from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<item_id>', views.add_to_basket, name='add_to_basket'),
    path('adjust/<item_id>', views.adjust_bag, name='adjust_bag'),
    path('remove/<item_id>', views.remove_from_bag, name='remove_from_bag'),
] 
