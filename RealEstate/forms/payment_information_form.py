from django.forms import ModelForm, widgets
from User.models import CreditCard


MONTHS = {
    'January': '01',
    'February': '02',
    'March': '03',
    'April': '04',
    'May': '05',
    'June': '06',
    'July': '07',
    'August': '08',
    'September': '09',
    'October': '10',
    'November': '11',
    'December': '12'
    }


class CreatePaymentForm(ModelForm):
    class Meta:
        model = CreditCard
        fields = '__all__'
        widgets = {
            'card_number': widgets.TextInput(attrs={'class': 'form-control', 'placeholder':'Card number'}),
            'month': widgets.Select(attrs={'class': 'form-control', 'placeholder': 'Month'}),
            'year': widgets.Select(attrs={'class': 'form-control', 'placeholder': 'Year'}),
            'cvc': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'CVC'})
        }
