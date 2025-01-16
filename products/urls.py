from django.urls import path
from . import views

# URLs configuration file,
# maps specific URL patterns to corresponding views in the app.
# This enables the application to respond appropriately,
# when a user accesses certain paths

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
]
