
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="real_estate"),
    path("real_estate_information", views.realEstateInformation, name="real_estate_information"),
    path("add_real_estate/", views.addRealEstatem, name="add_real_estate"),
    path("add_real_estate_confirmation/", views.addRealEstateCofirmation, name="add_real_estate_confirmation"),
    path("buy_confirmation", views.buyConfirmation, name="buy_confirmation"),
    path("your_real_estate/", views.yourRealEstate, name="your_real_estate")
]