from django.shortcuts import render

# Created views for bag app here.


def view_bag(request):
    """ A view to return the bag contents page """

    return render(request, 'bag/bag.html')
