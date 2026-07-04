from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order
from cart.models import CartItem


@login_required
def checkout(request):

    cart_items = CartItem.objects.filter(user=request.user)

    total = 0
    for item in cart_items:
        total += item.product.price * item.quantity

    # empty cart check (IMPORTANT)
    if not cart_items.exists():
        return redirect('/cart/')

    if request.method == "POST":

        Order.objects.create(
            user=request.user,   # ⭐ IMPORTANT
            customer_name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            address=request.POST['address'],
            total_amount=total
        )

        cart_items.delete()

        return redirect('/orders/success/')  # (or /success/ if you don't use payment page)

    return render(
        request,
        'orders/checkout.html',
        {'total': total}
    )


def order_success(request):
    return render(request, 'orders/success.html')