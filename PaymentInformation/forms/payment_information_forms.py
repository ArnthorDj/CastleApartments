from django.forms import ModelForm, widgets
from django import forms
from PaymentInformation.models import CreditCard

MONTHS = {
    'january':('01'),
    'febuary':('02'),
    'mars':('03'),
    'april':('04'),
    'may':('05'),
    'june':('06'),
    'july':('07'),
    'august':('08'),
    'september':('09'),
    'october':('10'),
    'november':('11'),
    'december':('12')
    }

class CreatePaymentform(ModelForm):
    class Meta:
        model = CreditCard
        fields = '__all__'
        widgets = {
            'card_number': widgets.TextInput(attrs={'class': 'form-control', 'placeholder':'Card number'}),
            'month': widgets.Select(attrs={'class': 'form-control', 'placeholder': 'Month'}),
            'year': widgets.Select(attrs={'class': 'form-control', 'placeholder': 'Year'}),
            'cvc': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'CVC'})
        }


