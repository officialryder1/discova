from django.shortcuts import render, redirect, get_object_or_404
from .models import Merchant
from store.models import Product, Category
from payment.models import ShippingAddress, Order, Transaction, Completed_order
from .form import Merchant_form, MessageAdmin_form
from payment.form import TransactionForm
from django.contrib.auth.models import User


def signup(request):
    if request.method == "POST":
        form = Merchant_form(request.POST, request.FILES)
        if form.is_valid():
            author = form.save(commit=False)
            author.author = request.user
            author.save()
            return redirect("home")
    else:
        form = Merchant_form()

    context = {'form':form}
    return render(request, 'merchant/merchant.html', context)

def dashboard(request):
    product = Product.objects.all()
    merchant = Merchant.objects.all()
    category = Category.objects.all()
    shipping = ShippingAddress.objects.all()
    order = Order.objects.all()
    transaction = Transaction.objects.all()
    users = User.objects.all()
    recent_joint_user = User.objects.all().order_by("-date_joined")[:5]
    product_added = Product.objects.all()[:5]

    context = {
        'product':product,
        'merchant':merchant,
        'category':category,
        'shipping':shipping,
        'order':order,
        'transaction':transaction,
        'users':users,
        'recent':recent_joint_user,
        'added_product':product_added,
    }
    return render(request, 'merchant/dashboad.html', context)

def merchant_dashboard(request):
    user = request.user
    merchant = Merchant.objects.get(author=user)
    product = Product.objects.filter(owner=merchant)
    transaction = Transaction.objects.filter(product__in=product)
    order = Completed_order.objects.filter(user=merchant)
    count = len(transaction) - 1
    

    context = {
        'user':user,
        'merchant':merchant,
        'product':product,
        'transaction':transaction,
        'order':order,
        'count':count
    }

    return render(request, 'merchant/merchant_dashboard.html', context)

def get_order(request):
    user = request.user
    users = User.objects.get(username=user)
    merchant = Merchant.objects.get(author=user)
    product = Product.objects.filter(owner=merchant)
    transaction = Transaction.objects.filter(product__in=product).order_by('product')
    shipping = ShippingAddress.objects.filter(user=users)
    
    
    if request.method == 'POST':
        ship = ShippingAddress.objects.get(user=request.user)
        trans = Transaction.objects.get(name=ship)
        date = request.POST['date']
        trans.status = "Approved"
        trans.delivery_date = date
        trans.save()
        completed = Completed_order.objects.create(user=merchant, transaction=trans)
        completed.save()
        return redirect('merchant_dashboard')
    context = {
        'user':user,
        'merchant':merchant,
        'product':product,
        'transaction':transaction,
        'shipping':shipping
        
    }

    return render(request, 'merchant/order.html', context)

def merchant_product(request):
    user = request.user
    merchant = Merchant.objects.get(author=user)
    product = Product.objects.filter(owner=merchant)

    content = {
        'user':user,
        'merchant':merchant,
        'product':product
    }

    return render(request, 'merchant/product.html', content)

def send_message(request):
    if request.method == 'POST':
        form = MessageAdmin_form(request.POST, request.FILES)
        if form.is_valid():
            author = form.save(commit=False)
            author.user = request.user
            author.save()
            return redirect("merchant_dashboard")
    else:
        form = MessageAdmin_form()
    context = {
        'form':form
    }
    return render(request, "merchant/send_feedback.html", context)
    
