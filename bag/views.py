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
    redirect_url = request.POST.get('redirect_url')
    size = None
    quantity = int(request.POST.get('quantity'))

    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
                messages.success(request, f'Updated Size {size.upper()} {product.name} quantity to {bag[bag_id]["items_by_size"][size]}!')
            else:
                bag[item_id]['items_by_size'][size] = quantity
                messages.success(request, f'Added size {size.upper()} {product.name} to your bag!')
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request, f'Added Size {size.upper()} {product.name} to your bag!')
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}!')
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag!')

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)
