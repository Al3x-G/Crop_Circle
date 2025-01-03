from django.shortcuts import render

# Created views for home app here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')
