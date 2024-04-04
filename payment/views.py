from django.shortcuts import render, redirect
from .models import ShippingAddress, Order, Transaction
from .form import Shipping
from cart.cart import Cart
from django.contrib.auth.decorators import login_required


def payment_success(request):
    return render(request, 'payment/payment.html')

@login_required(login_url="login")
def shipping_form(request):
    if request.method == "POST":
        form = Shipping(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.user = request.user
            author.save()
            return redirect("checkout")
    else:
        form = Shipping()

    context = {'form':form}
    return render(request, 'payment/update_shipping.html', context)

@login_required(login_url="login")
def update_info(request):
    user = request.user
    post = ShippingAddress.objects.get(user=user)
    if request.method == "POST":
        form = Shipping(request.POST, instance=post)
        if form.is_valid():
            author = form.save(commit=False)
            author.user = request.user
            author.save()
            return redirect("checkout")
    else:
        form = Shipping(instance=post)

    context = {'form':form}
    return render(request, 'payment/checkout_form.html', context)

@login_required(login_url="login")
def checkout(request):
    cart = Cart(request)
    cart_product = cart.get_probs
    quantities = cart.get_quants
    total = cart.cart_total
    user = request.user
    post = ShippingAddress.objects.get(user=user)
    if request.method == "POST":
        form = Shipping(request.POST, instance=post)
        if form.is_valid():
            author = form.save(commit=False)
            author.user = request.user
            author.save()
            return redirect("checkout")
    else:
        form = Shipping(instance=post)
    return render(request, 'payment/checkout.html', {'cart_product':cart_product, 'quantities':quantities, 'total':total, 'form':form})