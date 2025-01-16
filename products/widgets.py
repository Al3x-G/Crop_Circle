from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    """
    A custom widget for handling file input fields in forms.
    Extends Django's ClearableFileInput to customise the appearance and behavior.
    """
    # Label for the checkbox used to clear/remove the currently uploaded file
    clear_checkbox_label = _('Remove')

    # Text displayed next to the currently uploaded file
    initial_text = _('Current Image')

    # Text displayed next to the file input field (empty here for customisation)
    input_text = _('')

    # Path to the custom widget template for rendering this input field
    template_name = 'products/custom_widget_templates/custom_clearable_file_input.html'
