from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages

from products.models import Product

# Created views for bag app here.


def view_bag(request):
    """ View to return the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ This function handles adding a product to the shopping bag."""

    # Retrieve the product quantity and redirect URL from the POST request.
    # If the product already exists in the bag (stored in the session),
    # increment the quantity; otherwise,
    # add the product with the specified quantity.
    # The updated bag is saved back into the session,
    # and the user is redirected to the specified URL.

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request,
                         (f'Updated {product.name} '
                          f'quantity to {bag[item_id]}'))
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    # Retrieve the product using the provided item_id.
    # If not found, a 404 error is raised.
    # Get the new quantity from the POST request and convert it to an integer.
    # Retrieve bag from the session, if not found initialise as empty dict.
    # Check if the new quantity is greater than 0.
    # If so, update the quantity of the product in the bag.
    # Set the new quantity for the product in the bag,
    # Success message sent to the user.
    # If the quantity is 0 or less, remove the product from the bag,
    # Success message sent to the user.
    # The updated bag is saved back into the session,
    # and the user is redirected to the specified URL.

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request,
                         (f'Updated {product.name} '
                          f'quantity to {bag[item_id]}'))
    else:
        bag.pop(item_id)
        messages.success(request,
                         (f'Removed {product.name} '
                          f'from your bag'))

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    # Retrieve the product using the provided item_id.
    # If not found, a 404 error is raised.
    # Retrieve bag from the session, if not found initialize as empty dict.
    # Remove the item from the bag using its item_id.
    # Success message sent to the user.
    # Update the session with the modified bag (without the removed item).
    # Return HTTP response (status 200) to indicate operation was successful.
    # If any error occurs, display an error message.
    # Return HTTP response (status 500) to indicate an internal server error.

    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})

        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
