from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .forms import UserProfileForm
from .models import UserProfile


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
