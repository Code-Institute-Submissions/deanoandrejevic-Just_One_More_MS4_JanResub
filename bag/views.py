from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from products.models import Product

# Create your views here.

def view_bag(request):
    """
    This will display the bag page.
    """

    return render(request, 'bag/bag.html')


def add_to_basket(request, item_id):
    """
    This view will allow user to add item to the bag and will give a total
    """

    product = get_object_or_404(Product, pk=item_id)