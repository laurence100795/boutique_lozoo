from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, 'theres nothing in your bag at the moment')
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51H7NrpEfDB6nIOBgPpSlLJ64jAe7j853XqDQZuiIkv1keEnkCKGIsbGtm5eOiS3PDmA5dkpjPnwgd2OiY7zoqdLJ00YsG5iAFK',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
