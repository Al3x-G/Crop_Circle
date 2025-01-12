from django.urls import path
from . import views
from .webhooks import webhook

# URLs configuration file,
# maps specific URL patterns to corresponding views in the app.
# This enables the application to respond appropriately,
# when a user accesses certain paths

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_number>',
         views.checkout_success,
         name='checkout_success'),
    path('wh/', webhook, name='webhook')
]
