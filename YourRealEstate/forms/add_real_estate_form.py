from django.forms import ModelForm, widgets
from RealEstate.models import RealEstates


class AddRealEstateForm(ModelForm):
    class Meta:
        # image = forms.CharField(required=True, widgets=forms.TextInput(attrs={'class':'form-control'}))
        model = RealEstates
        exclude = ['id', 'on_sale', 'seller_id']
        # fields = "__all__"
        widgets = {
            'street': widgets.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 16em'}),
            'city': widgets.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 16em'}),
            'zip_code': widgets.Select(attrs={'class': 'form-control', 'style': 'max-width: 16em'}),
            'size': widgets.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 16em'}),
            'bedrooms': widgets.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 16em'}),
            'bathrooms': widgets.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 16em'}),
            'type': widgets.Select(attrs={'class': 'form-control', 'style': 'max-width: 16em'}),
            'price': widgets.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 16em'})
        }
