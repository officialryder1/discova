from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import ShippingAddress, Transaction, Order

class Shipping(forms.ModelForm):

    class Meta:
        model = ShippingAddress
        fields = ['full_name', 'email', 'number', 'address_1', 'address_2', 'city', 'state', 'country']

        widgets = {
            'full_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Full Name'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
            'number': forms.NumberInput(),
            'address_1': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address !'}),
            'address_2': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address 2'}),
            'city': forms.TextInput(attrs={'class':'form-control', 'placeholder':'City'}),
            'state': forms.TextInput(attrs={'class':'form-control', 'placeholder':'State'}),
            'country': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Country'}),

        }



class TransactionForm(forms.ModelForm):

    class Meta:
        model = Transaction
        fields = ['delivery_date']

        widgets = {
            'delivery_date':forms.DateTimeInput(attrs={'class':'form-control'})
        }