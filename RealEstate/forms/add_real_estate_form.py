from django.forms import ModelForm, widgets
from RealEstate.models import RealEstates, RealEstateImages
from django.contrib.auth.models import User


class AddRealEstateForm(ModelForm):
    class Meta:
        # image = forms.CharField(required=True, widgets=forms.TextInput(attrs={'class':'form-control'}))
        model = RealEstates
        exclude = ['id', 'on_sale', 'seller_id', 'employee']
        # fields = "__all__"
        widgets = {
            'street': widgets.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 20em'}),
            'city': widgets.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 20em'}),
            'zip_code': widgets.Select(attrs={'class': 'form-control', 'style': 'max-width: 20em'}),
            'size': widgets.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 20em'}),
            'bedrooms': widgets.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 20em'}),
            'bathrooms': widgets.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 20em'}),
            'type': widgets.Select(choices=[
                ("Beach House", "Beach House"),
                ("Single Family Home", "Single Family Home"),
                ("Summer House", "Summer House"),
                ("Condo House", "Condo House"),
                ("Apartment Building", "Apartment Building"),
                ("Townhouse", "Townhouse"),
                ("Villas", "Villas")
            ] ,attrs={'class': 'form-control','choices':'COLOR_CHOICES', 'style': 'max-width: 20em'}),
            'price': widgets.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 20em'}),
            'more_info': widgets.Textarea(attrs={'class': 'form-control', 'style': 'width: 20em; height: 10em;'}),
            'main_image': widgets.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 20em'})
        }


class AddRealEstateImage(ModelForm):
    class Meta:
        # image = forms.CharField(required=True, widgets=forms.TextInput(attrs={'class':'form-control'}))
        model = RealEstateImages
        # fields = "__all__"
        exclude = ['id', 'real_estate']
        widgets = {
            'image': widgets.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 20em'}),
            'image2': widgets.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 20em'}),
            'image3': widgets.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 20em'}),
            'image4': widgets.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 20em'}),
            'image5': widgets.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 20em'}),
            'image6': widgets.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 20em'}),
        }

