from django.shortcuts import render, redirect
from .models import Product, Category
from merchant.models import Merchant
from payment.models import ShippingAddress
from .form import RegisterUser
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .form import UploadProduct
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



def Home(request):
    
    product = Product.objects.all()
    category = Category.objects.all()
    mobile = Product.objects.filter(category=4)[:5]
    watch = Product.objects.filter(category=1)[:5]
    jeweries = Product.objects.filter(category=2)[:5]
    cloth = Product.objects.filter(category=3)[:5]

    content = {
        'product':product,
        'category':category,
        'mobile':mobile,
        'watch':watch,
        'jeweries':jeweries,
        'cloth':cloth,
    }
    return render(request, 'store/index.html', content)

def Store(request):
    product = Product.objects.all()
    category = Category.objects.all()
    mobile = Product.objects.filter(category=4)
    watch = Product.objects.filter(category=1)
    jeweries = Product.objects.filter(category=2)
    cloth = Product.objects.filter(category=3)

    content = {
        'product':product,
        'category':category,
        'mobile':mobile,
        'watch':watch,
        'jeweries':jeweries,
        'cloth':cloth
    }

    return render(request, 'store/store.html', content)

def detail(request, pk):
    product = Product.objects.get(id=pk)
    category = Category.objects.all()

    content = {
        'product':product,
        'category':category,
        
    }

    return render(request, 'store/detail_page.html', content)

def category(request, cat):
    category = Category.objects.all()
    name = Category.objects.get(name=cat)
    product = Product.objects.filter(category=name)

    content = {
        'product':product,
        'cat':cat,
        'category':category,
        'name':name
    }

    return render(request, 'store/category.html', content)

def search(request):
    if request.method == "POST":
        search = request.POST['searched']
        product = Product.objects.filter(name__contains=search)
        content = {
            'search':search,
            'product':product
        }

        return render(request, 'store/search.html', content)

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("There was error logging into this Account"))
            return redirect("login")
    
    else:
        return render(request, 'store/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You Are Logout, Try Login Again"))
    return redirect('home')

def register_user(request):
    if request.method =="POST":
        form = RegisterUser(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,("Registration Successful"))
            return redirect('home')
    else:
        form = RegisterUser()
    return render(request, 'store/registration.html', {'form':form})

@login_required(login_url="login")
def upload_product(request):
    if request.method == "POST":
        form = UploadProduct(request.POST, request.FILES)
        if form.is_valid():
            author = form.save(commit=False)
            user = User.objects.get(username=request.user)
            merchant = Merchant.objects.get(author=user)
            author.owner = merchant
            author.save()
            return redirect("home")
    else:
        form = UploadProduct()

    context = {'form':form}
    return render(request, 'store/upload_product.html', context)

@login_required(login_url="login")
def update_product(request, pk):
    post = Product.objects.get(id=pk)
    if request.method =="POST":
        form = UploadProduct(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UploadProduct(instance=post)
    
    return render(request, 'store/update_product.html', {'form':form})

@login_required(login_url="login")
def delete(request, pk):
    post = Product.objects.get(id=pk)
    post.delete()
    return redirect('home')

def Profile(request):
    user = request.user
    try:
        if user.is_authenticated:
            shipping = ShippingAddress.objects.get(user=user)
            context = {
                'shipping':shipping,
            }
            return render(request, 'store/profile.html', context)
        else:
            return render(request, 'store/profile.html')
    except:
        return render(request, 'store/profile.html')
    