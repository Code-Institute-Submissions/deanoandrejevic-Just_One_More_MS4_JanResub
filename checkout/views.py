from django.shortcuts import render

# Create your views here.

def checkout(request):
    """
    This will display the bag page.
    """

    return render(request, 'checkout/checkout.html')
