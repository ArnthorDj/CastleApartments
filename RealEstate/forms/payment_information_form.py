from django.forms import ModelForm, widgets
from User.models import CreditCard


MONTHS = {
    '1':'January',
    '2':'February',
    '3':'March',
    '4':'April',
    '5':'May',
    '6':'June',
    '7':'July',
    '8':'August',
    '9':'September',
    '10':'October',
    '11':'November',
    '12':'December'
    }


class CreatePaymentForm(ModelForm):
    class Meta:
        model = CreditCard
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'card_number': widgets.TextInput(attrs={'class': 'form-control', 'placeholder':'Card number'}),
            'month': widgets.SelectDateWidget(months=MONTHS, years=None, attrs={'class': 'form-control', 'placeholder': 'Month'}),
            'year': widgets.Select(attrs={'class': 'form-control', 'placeholder': 'Year'}),
            'cvc': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'CVC'})
        }
