from django.contrib import admin
from .models import Order, OrderLineItem


# Define the inline admin class for the OrderLineItem model. This allows the
# related line items to be displayed and managed inside the Order admin page.
class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    # Define the fields that will be readonly for this inline
    readonly_fields = ('lineitem_total',)


# Define the admin interface for the Order model
class OrderAdmin(admin.ModelAdmin):
    # Include the OrderLineItemAdminInline in the Order admin page,
    # so related order items can be viewed/edited inline
    inlines = (OrderLineItemAdminInline,)

    # Define the fields that will be read-only in the admin panel.
    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total', 'grand_total',
                       'original_bag', 'stripe_pid',)

    # Define the fields that will be displayed when
    # creating or editing an Order in the admin interface
    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'grand_total', 'original_bag', 'stripe_pid',)

    # Define how the orders should be displayed.
    # These are the fields that will appear as columns in the list view
    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total', 'original_bag', 'stripe_pid',)

    # Define ordering of orders in the admin interface (by descending date)
    # This means orders will be listed from the most recent to the oldest
    ordering = ('-date',)  # The minus sign indicates descending order


# Register the Order model and its custom admin class to the admin site
admin.site.register(Order, OrderAdmin)
