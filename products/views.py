from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

# Create your views here.

def products(request):
    """
    This view will show all the products as well as search
    querys and sorting results
    """

    context = {
        'products': products
    }

    return render(request, 'products/products.html')
