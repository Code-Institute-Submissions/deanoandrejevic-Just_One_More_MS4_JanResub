from django.shortcuts import render, redirect, reverse, get_object_or_404

# Create your views here.

def view_bag(request):
    """
    This will display the bag page.
    """

    return render(request, 'bag/bag.html')