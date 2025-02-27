from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime
from pymongo import MongoClient
from django.conf import settings
from cart.models import CartItem
from orders.models import Order
from decimal import Decimal

client = MongoClient(settings.DATABASES['ecommercedb']['CLIENT']['host'])
db = client.ecommercedb

@login_required
def order_preview(request):
    customer = request.user

    items = CartItem.objects.using('cartdb').filter(cart__customer_id=customer.id, is_ordered=False)
    if not items:
        messages.error(request, "Your cart is empty!")
        return redirect('cart')

    subtotal = sum(item.price * item.quantity for item in items)

    discount = 0
    total = subtotal

    coupon_code = request.POST.get('coupon')
    if coupon_code:
        coupon = db.coupon.find_one({
            'code': coupon_code,
            'customer_type': customer.customer_type,
            'is_active': True,
            'usage_limit': {'$gt': 0},
            'valid_from': {'$lte': datetime.now()},
            'valid_to': {'$gte': datetime.now()}
        })
        if coupon:
            discount_value = float(coupon['discount_value'].to_decimal())
            if coupon['discount_type'] == 'percent':
                discount = (discount_value / 100) * float(subtotal)
            else:
                discount = discount_value

            subtotal = Decimal(subtotal)
            discount = Decimal(discount)
            
            total = subtotal - discount
            messages.success(request, f"Coupon applied! You saved ${discount:.2f}")
        else:
            messages.error(request, "Invalid or ineligible coupon.")

    available_coupons = db.coupon.find({
        'customer_type': customer.customer_type,
        'is_active': True,
        'usage_limit': {'$gt': 0},
        'valid_from': {'$lte': datetime.now()},
        'valid_to': {'$gte': datetime.now()}
    })

    return render(request, 'orders/confirmation.html', {
        'items': items,
        'subtotal': subtotal,
        'discount': discount,
        'total': total,
        'available_coupons': available_coupons,
        'coupon_code': coupon_code
    })


@login_required
def confirm_order(request):
    customer = request.user

    items = CartItem.objects.using('cartdb').filter(cart__customer_id=customer.id, is_ordered=False)
    if not items:
        messages.error(request, "Your cart is empty!")
        return redirect('cart')

    subtotal = sum(item.price * item.quantity for item in items)

    discount = float(request.POST.get('discount', 0))
    total = float(request.POST.get('total', subtotal))
    shipping_address = request.POST.get('shipping_address')
    status = request.POST.get('status', 'packing')

    # Lưu order vào DB
    order = Order.objects.using('cartdb').create(
        customer_id=customer.id,
        subtotal=subtotal,
        discount=discount,
        total=total,
        shipping_address=shipping_address,
        status=status
    )

    order.items.set(items)
    items.update(is_ordered=True)

    messages.success(request, "Order placed successfully!")
    return redirect('shop')


@login_required
def order_list(request):
    orders = Order.objects.using('cartdb').filter(customer_id=request.user.id).order_by('-created_at')
    return render(request, 'orders/order_list.html', {'orders': orders})

@login_required
def delete_order(request, order_id):
    order = Order.objects.using('cartdb').filter(id=order_id, customer_id=request.user.id).first()

    if order:
        order.delete(using='cartdb')
        messages.success(request, "Order cancelled successfully.")
    else:
        messages.error(request, "Order not found or permission denied.")

    return redirect('order_list')