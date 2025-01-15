from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .forms import UserProfileForm
from .models import UserProfile
from checkout.models import Order


def profile(request):
    """
    Display the user's profile and allow updates to profile information.

    - Handles displaying the form and updating user profile,
    if the form is submitted with valid data.
    """
    # Retrieve the user's profile or return a 404 error if not found
    profile = get_object_or_404(UserProfile, user=request.user)

    # Check if the form has been submitted (POST request)
    if request.method == 'POST':
        # Bind the form with the submitted data and existing profile instance
        form = UserProfileForm(request.POST, instance=profile)

        # If the form is valid, save the changes to the profile
        if form.is_valid():
            form.save()
            # Display a success message to the user
            messages.success(request, 'Profile updated successfully')

    # If not a POST request (GET), create a form for displaying current profile
    form = UserProfileForm(instance=profile)

    # Retrieve all orders associated with the user's profile
    orders = profile.orders.all()

    # Define the template and context to render
    template = 'profiles/profile.html'
    context = {
        'form': form,  # The profile form to be rendered
        'orders': orders,  # The user's orders to be displayed
        'on_profile_page': True,  # Flag indicating user is on their profile
    }

    # Render the template with the provided context (form and orders)
    return render(request, template, context)


def order_history(request, order_number):
    """
    View to display the details of a specific past order.
    - Retrieves the order using the provided order number.
    - Displays a confirmation message about the order.
    - Renders the order details in a success page template.
    """

    # Fetch order object using the order_number, or return a 404 if not found
    order = get_object_or_404(Order, order_number=order_number)

    # Add an informational message for the user about the order
    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    # Define the template to be used for rendering the order details
    template = 'checkout/checkout_success.html'

    # Context to pass to the template, including the order and
    # a flag to indicate this is accessed from the profile
    context = {
        'order': order,  # The specific order to be displayed
        'from_profile': True,  # Flag indicates view was via the user's profile
    }

    # Render the template with the given context and return the response
    return render(request, template, context)
