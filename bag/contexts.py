from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

"""
Define the function bag_contents that will calculate the contents of the
shopping bag, based on the user's request
(this could include items, total cost, delivery, etc.)
"""


def bag_contents(request):

    # Initialize an empty list to hold the items in the shopping bag
    bag_items = []

    # Initialize total amount spent so far to 0
    total = 0

    # Initialize the product count to 0
    product_count = 0

    # Access shopping bag in session (if exists) or an empty dict if not
    bag = request.session.get('bag', {})

    # Loop through shopping bag, calculate total price and product count,
    # Create a list of dictionaries containing
    # product details, quantity, and item ID.
    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)  # Find product id
        total += quantity * product.price  # Add cost of the current item
        product_count += quantity  # Increment the total product count
        bag_items.append({  # Append product details to the list for later use
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
            })

    # Check if total is less than the free delivery threshold (from settings)
    if total < settings.FREE_DELIVERY_THRESHOLD:
        # If the total is less than the free delivery threshold,
        # calculate the standard delivery charge.
        # Delivery percentage is retrieved from settings
        # and divided by 100 to make it a decimal.
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)

        # Calculate the difference to reach the free delivery threshold
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        # If the total is greater than or equal to
        # the free delivery threshold, no delivery charge.
        delivery = 0
        # Do not add anything to the free_delivery_delta since delivery is free
        free_delivery_delta = 0

    # Calculate the grand total by adding the
    # delivery charge (if any) to the total cost
    grand_total = delivery + total

    # Prepare the context dictionary that will be passed to the template,
    # This contains all the information the
    # template needs to display to the user
    context = {
        'bag_items': bag_items,  # Items in the shopping bag (empty for now)
        'total': total,  # The total cost of the items in the shopping bag
        'product_count': product_count,  # The number of products in the bag
        'delivery': delivery,  # The delivery charge, calculated above
        'free_delivery_delta': free_delivery_delta,  # Amount for free delivery
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,  # The grand total with delivery charge
    }

    # Return the context dictionary to be used in rendering the template,
    # In every app across the entire project
    return context
