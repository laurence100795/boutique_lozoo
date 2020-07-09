from django.shortcuts import render


def view_bag(request):
    """ A view that renders the bad contents page"""
    return render(request, 'bag/bag.html')
