from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Krq7vKJ8euVo6nxijuWdkyNhX94CgbsFTnDnFwn9iEtoHlVWms5eFmObAnCKU2vMOg5bWVl2ha9EWLQCy7jf7QP00RSuspx9h',
        'client_secret': 'sk_test_51Krq7vKJ8euVo6nxQDsUU58nIdInidYTenYVlzjjP8SrXn214abGEXE5putOzqBtMYCAzjQuiZkXvSsiRBiqbLrE004eRQC2mO',
    }

    return render(request, template, context)