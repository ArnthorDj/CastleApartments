from django.forms import ModelForm, widgets
from AddRealEstate.models import NewRealEstate
from django import forms

class AddRealEstateForm(ModelForm):
    class Meta:
        #image = forms.CharField(required=True, widgets=forms.TextInput(attrs={'class':'form-control'}))
        model: NewRealEstate
        exclude = ['id', 'on_sale', 'seller_id']
        #fields = "__all__"
        widgets = {
            'street': widgets.TextInput(attrs={'class':'form-control'}),
            'city': widgets.TextInput(attrs={'class':'form-control'}),
            'zip_code': widgets.Select(attrs={'class':'form-control'}),
            'size': widgets.TextInput(attrs={'class':'form-control'}),
            'bedrooms': widgets.TextInput(attrs={'class':'form-control'}),
            'type': widgets.Select(attrs={'class':'form-control'}),
            'price': widgets.TextInput(attrs={'class':'form-control'})
        }

