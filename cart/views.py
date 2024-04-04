from django.shortcuts import render, get_object_or_404, redirect
from store.models import Category, Product
from .models import *
from .cart import Cart
from django.http import JsonResponse
from django.contrib import messages


def cart_info(request):
    cart = Cart(request)
    cart_product = cart.get_probs
    quantities = cart.get_quants
    total = cart.cart_total
    
    return render(request, 'cart/cart.html', {'cart_product':cart_product, 'quantities':quantities, 'total':total})

def add(request):
    cart = Cart(request)
    # test for post
    if request.POST.get('action') == 'post':
        # get stuff
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        # look up product in database
        product = get_object_or_404(Product, id=product_id)
        #now save to a sessiom 
        cart.add(product=product, quantity=product_qty)
        # Get cart Quantity
        cart_quantity= cart.__len__()

        # return responds
        # response = JsonResponse({'Product Name: ': product.name})
        
        response = JsonResponse({'qty: ': cart_quantity})
        messages.success(request, ("Product Added to Cart"))
        return response

def edit(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        # get stuff
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        cart.update(product=product_id, quantity=product_qty)

        response = JsonResponse({'qty':product_qty})
        return response


def delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        # get stuff
        product_id = int(request.POST.get('product_id'))
        

        cart.delete(product=product_id)

        response = JsonResponse({'product':product_id})
        messages.success(request, ("Product has been deleted"))
        return response