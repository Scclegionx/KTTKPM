from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cart.models import Cart, CartItem
from customer.models import Customer
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404

@login_required
def cart_view(request):
    customer_id = request.user.id

    cart, created = Cart.objects.using('cartdb').get_or_create(customer_id=customer_id)

    items = CartItem.objects.using('cartdb').filter(cart=cart, is_ordered=False)

    return render(request, 'cart/cart.html', {'cart': cart, 'items': items})


@login_required
def add_to_cart(request, product_id, product_name, price):
    customer_id = request.user.id
    cart, created = Cart.objects.using('cartdb').get_or_create(customer_id=customer_id)

    # Kiểm tra nếu item đã order rồi -> Tạo mới item
    existing_item = CartItem.objects.using('cartdb').filter(cart=cart, product_id=product_id, is_ordered=False).first()

    if existing_item:
        # Nếu item chưa order, tăng số lượng
        existing_item.quantity += 1
        existing_item.save(using='cartdb')
    else:
        # Tạo mới nếu chưa có hoặc item cũ đã order
        CartItem.objects.using('cartdb').create(
            cart=cart,
            product_id=product_id,
            product_name=product_name,
            price=price,
            quantity=1,
            is_ordered=False
        )

    messages.success(request, f"{product_name} added to cart!")
    return redirect(request.META.get('HTTP_REFERER', 'shop'))


@login_required
def update_cart_item(request, item_id):
    item = get_object_or_404(CartItem.objects.using('cartdb'), id=item_id, cart__customer_id=request.user.id)

    new_quantity = int(request.POST.get('quantity'))
    if new_quantity > 0:
        item.quantity = new_quantity
        item.save(using='cartdb')
        messages.success(request, f"Updated {item.product_name} quantity!")
    else:
        messages.error(request, "Quantity must be at least 1.")

    return redirect('cart')


@login_required
def delete_cart_item(request, item_id):
    item = get_object_or_404(CartItem.objects.using('cartdb'), id=item_id, cart__customer_id=request.user.id)
    item.delete(using='cartdb')
    messages.success(request, f"{item.product_name} removed from cart!")

    return redirect('cart')