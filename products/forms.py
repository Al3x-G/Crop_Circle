from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category


class ProductForm(forms.ModelForm):
    """
    Form for creating and updating Product instances.
    - Includes all fields from the Product model.
    - Allows customisation of the category choices and image field widget.
    """

    class Meta:
        # Specify the model and fields to use in the form.
        model = Product
        fields = '__all__'  # Include all fields from the Product model.

    # Define the image field with a custom widget for file input.
    image = forms.ImageField(
        label='Image',  # Label for the image field.
        required=False,  # Image is optional.
        widget=CustomClearableFileInput  # Widget for clearable file input.
    )

    def __init__(self, *args, **kwargs):
        """
        Initialise the form.
        - Dynamically set category choices using friendly names.
        - Add custom CSS classes to form fields for styling.
        """
        super().__init__(*args, **kwargs)

        # Fetch all categories from the database.
        categories = Category.objects.all()

        # Create a list of tuples with category IDs and their friendly names.
        # list comprehension = shorthand for loop that adds items to list.
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        # Set the choices for the category field using friendly names.
        self.fields['category'].choices = friendly_names

        # Loop through all fields in the form and add custom CSS classes.
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
