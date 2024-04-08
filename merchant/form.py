from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Merchant, MessageAdmin

class Merchant_form(forms.ModelForm):

    class Meta:
        model = Merchant
        fields = ['image','address', 'city', 'state', 'country', 'phone']

        widgets = {
            'address': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address'}),
            'city': forms.TextInput(attrs={'class':'form-control', 'placeholder':'City'}),
            'state': forms.TextInput(attrs={'class':'form-control', 'placeholder':'State'}),
            'country': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Country'}),
            'phone': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Phone'}),

        }


class MessageAdmin_form(forms.ModelForm):

    class Meta:
        model = MessageAdmin
        fields = ['detail', 'message', 'image']

        widgets = {
            'detail': forms.TextInput(attrs={'class':'form-control', 'placeholder':"Message Title"}),
            'message': forms.Textarea(attrs={'class':'form-control', 'placeholder':"Message"}),
        }
