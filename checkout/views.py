from django.shortcuts import (
    render, redirect, reverse
)
from django.contrib import messages

from .forms import OrderForm

# Created views for the checkout app here.


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Looks like there is nothing in your bag.")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_TYooMQauvdEDq54NiTphI7jx',
        'client_secret': 'CLIENT_SECRET',
    }

    return render(request, template, context)
