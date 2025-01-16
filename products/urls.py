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
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),  # noqa: E501 (Fix flake 8 line too long)
]
