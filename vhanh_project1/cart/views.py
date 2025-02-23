from django.shortcuts import render
from cart.models import Cart

def cart_list_view(request):
    carts = Cart.objects.all()
    return render(request, 'cart/cart_list.html', {'carts': carts})
