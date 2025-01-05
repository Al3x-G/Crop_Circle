from django.shortcuts import render, redirect

# Created views for bag app here.


def view_bag(request):
    """ View to return the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ This function handles adding a product to the shopping bag."""

    # It retrieves the product quantity and redirect URL from the POST request.
    # If the product already exists in the bag (stored in the session),
    # it increments the quantity; otherwise,
    # it adds the product with the specified quantity.
    # The updated bag is saved back into the session,
    # and the user is redirected to the specified URL.

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)
