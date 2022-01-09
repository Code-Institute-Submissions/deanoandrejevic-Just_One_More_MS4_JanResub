from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from .forms import OrderForm

# Create your views here.

def checkout(request):
    """
    This will display the bag page.
    """

    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag")

    order_form = OrderForm()

    template = 'checkout/checkout.html'

    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51K08mLBRYqT3cZ1NVVD3DTMjakcor32LEbhnP4Xd1auWF4a4YQnnUwaB6tR3abocI1pkZ98MyDmxf1VRV1GNhqpq00QS5RHGWH',
        'client_secret': 'client secret'
    }

    return render(request, template, context)
