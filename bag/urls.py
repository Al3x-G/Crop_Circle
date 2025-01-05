from django.urls import path
from . import views

# URLs configuration file,
# maps specific URL patterns to corresponding views in the app.
# This enables the application to respond appropriately,
# when a user accesses certain paths

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),
]
