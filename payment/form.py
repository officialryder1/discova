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



class BillingForm(forms.Form):
    card_name = forms.CharField( label= "", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Card Name'}), required=True),
    card_number = forms.IntegerField(label="", widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Card Number'}), required=True),
    card_exp_date = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Expiration Date'}), required=True),
    card_cvv_number = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'CVV'}), required=True),
    card_address1 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Billing Address'}), required=True),
    card_city = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'City'}), required=True),
    card_state = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'State'}), required=True),
    card_zipcode = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Zipcode'}), required=True),
    card_country = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Country'}), required=True),