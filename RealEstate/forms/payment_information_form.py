from django.forms import ModelForm, widgets
from User.models import CreditCard
import datetime



class CreatePaymentForm(ModelForm):
    class Meta:
        model = CreditCard
        # fields = '__all__'
        exclude = ['user']
        year = int(datetime.datetime.now().year)
        widgets = {
            'card_number': widgets.TextInput(attrs={'class': 'form-control', 'placeholder':'Card number','style': 'max-width: 20em'}),
            'month': widgets.Select(choices=[
                ('1', 'January'),
                ('2', 'February'),
                ('3', 'March'),
                ('4', 'April'),
                ('5', 'May'),
                ('6', 'June'),
                ('7', 'July'),
                ('8', 'August'),
                ('9', 'September'),
                ('10', 'October'),
                ('11', 'November'),
                ('12', 'December')], attrs={'class': 'form-control', 'placeholder': 'Month'}),
            'year': widgets.Select(choices=[(year, year) for year in range(year, year+5)], attrs={'class': 'form-control', 'placeholder': 'Year'}),
            'cvc': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'CVC'})
        }
