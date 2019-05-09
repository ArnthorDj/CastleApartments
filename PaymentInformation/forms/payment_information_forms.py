from django.forms import ModelForm, widgets
from django import forms
from PaymentInformation.models import CreditCard

class CreatePaymentform(ModelForm):
    class Meta:
        model = CreditCard
        fields = '__all__'
        widgets = {
            'card_number': widgets.TextInput(attrs={'class': 'form-control', 'placeholder':'Card number'}),
            'month': widgets.Select(attrs={'class': 'form-control', 'placeholder': 'Month'}),
            'year': widgets.Select(attrs={'class': 'form-control', 'placeholder': 'Year'}),
            'cvc': widgets.TextInput(attrs={'class': 'form-control', 'place-holder': 'cvc'})
        }
