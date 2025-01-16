from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category

from django.contrib.auth.decorators import login_required
from .forms import ProductForm

# Created views for product app here here.


def all_products(request):
    """ View to show all products, sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please specify what you're looking for to start your search!")  # noqa: E501 (Fix flake 8 line too long)
                return redirect(reverse('products'))

            # Using Q model OR operator
            queries = Q(name__icontains=query) | Q(description__icontains=query)  # noqa: E501 (Fix flake 8 line too long)
            products = products.filter(queries)

    # Return sorting method back to the template
    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ View to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """
    Add a new product to the store.
    - Only accessible to superusers.
    - Handles both GET and POST requests for the product creation form.
    """
    # Check if the user is a superuser
    if not request.user.is_superuser:
        # Display an error message and redirect to home page if not authorised
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        # Create a form instance with POST data and uploaded files
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form to create a new product instance
            product = form.save()
            # Display a success message
            messages.success(request, 'Successfully added product!')
            # Redirect to the product detail page for the newly added product
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            # Display an error message if the form is invalid
            messages.error(request,
                           ('Failed to add product. '
                            'Please ensure the form is valid.'))
    else:
        # Initialise an empty product form for GET requests
        form = ProductForm()

    # Define the template to render
    template = 'products/add_product.html'

    # Pass the form to the template context
    context = {
        'form': form,
    }

    # Render the template with the given context
    return render(request, template, context)
