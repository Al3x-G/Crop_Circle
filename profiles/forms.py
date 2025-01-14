from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """
    A form for updating the UserProfile model.
    This form excludes the 'user' field since that should never change.
    """
    class Meta:
        model = UserProfile  # Links the form to the UserProfile model
        exclude = ('user',)  # Excludes the 'user' field from the form

    def __init__(self, *args, **kwargs):
        """
        Customizes the form during initialisation:
        - Adds placeholders to the fields for user guidance.
        - Adds CSS classes for consistent styling.
        - Removes auto-generated labels for a cleaner appearance.
        - Sets autofocus on the first input field.
        """
        super().__init__(*args, **kwargs)

        # Dictionary mapping field names to placeholder text
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

        # Set autofocus on the first field (default_phone_number)
        self.fields['default_phone_number'].widget.attrs['autofocus'] = True

        # Iterate over all fields in the form
        for field in self.fields:
            # Skip adding placeholder for the 'default_country' field
            if field != 'default_country':
                # Add an asterisk to required fields in the placeholder
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                # Set the placeholder attribute for the field
                self.fields[field].widget.attrs['placeholder'] = placeholder

            # Add custom CSS classes for styling the input fields
            self.fields[field].widget.attrs['class'] = (
                'border-black rounded-0 profile-form-input'
            )

            # Remove the default label for the field
            self.fields[field].label = False
