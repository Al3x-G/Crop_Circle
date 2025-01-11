from django import forms
from .models import Order


# This form is associated with the Order model.

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order  # The model this form is associated with.

        # Specifies the fields that should appear in the form.
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)

    # Custom initialisation method to modify form field attributes.
    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes to the form fields,
        remove auto-generated labels, and set autofocus on the first field.
        """
        super().__init__(*args, **kwargs)  # Call the parent class initialiser.

        # Define the placeholders for each field,
        # to provide helpful hints to the user.
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County, State or Locality',
        }

        # Set autofocus on the first field (full_name).
        self.fields['full_name'].widget.attrs['autofocus'] = True

        # Loop over all the fields in the form and set attributes.
        for field in self.fields:
            # Skip the 'country' field from placeholder assignment.
            if field != 'country':
                # Set placeholders for required and optional fields.
                # Add '*' for required fields.
                # Assign placeholder text.
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder

            # Add a custom CSS class to the field for styling.
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'

            # Disable the auto-generated labels by setting the label to False
            self.fields[field].label = False
