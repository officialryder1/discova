from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product
from django.contrib.auth.forms import UserChangeForm


class RegisterUser(UserCreationForm):
   firstname = forms.CharField(max_length=200)

   class Meta:
        model = User
        fields = (
            'username', 'firstname','email', 'password1','password2'
        )
        help_texts = {
           k:"" for k in fields
        }

        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}),
            'firstname': forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
            'password1': forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}),
            'password2':forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Comfirm Password'})
        }


class UploadProduct(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'image','description', 'specification', 'category', 'color', 'price', 'location', 'stock', "is_available", 'is_sale', 'sale_price']

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Product Name'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}),
            'specification': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Specification'}),
            'category': forms.Select(attrs={'class':'form-control', 'placeholder':'Category'}),
            'color': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Color'}),
            'price': forms.NumberInput(),
            'location': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Location'}),
            'stock': forms.NumberInput(),
            'sale_price':forms.NumberInput(),
        }

class UserForm(UserChangeForm):

    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}),
            'firstname':forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),
            'lastname':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'})
        } 
        

