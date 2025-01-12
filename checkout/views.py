from django.shortcuts import (
    render, redirect, reverse
)
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from bag.contexts import bag_contents

import stripe

# Created views for the checkout app here.


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Looks like there is nothing in your bag.")
        return redirect(reverse('products'))

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_TYooMQauvdEDq54pk_test_51QgGfSGPAr31TKtuWLsYtlanGft2gHeDUNGHnr01WX1VpjFPqxMgsB9Ni62uODesAToBdFSjl2A5F78YqqsnA5t900Ly9FoR4KNiTphI7jx',  # noqa: E501 (Fix flake 8 line too long)
        'client_secret': 'CLIENT_SECRET',
    }

    return render(request, template, context)
