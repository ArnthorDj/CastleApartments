from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="real_estate"),
    path("info/<int:id>", views.get_real_estate_by_id, name="real_estate_information"),
    path("pay/<int:id>", views.payment_information, name="payment_information_index"),
    path("pay/<int:id>/confirmation/", views.payment_confirmation, name="payment_confirmation"),
    path("pay/<int:id>/bought/", views.bought_real_estate, name="bought"),
    path("add/", views.add_real_estate_images, name="real_estate_image"),
    path("add_images/<int:id>", views.add_real_estate, name="add_real_estate_index"),
    # path("add/confirmation/", views.addRealEstateConfirmation, name="add_real_estate_confirmation"),
    # path("your_real_estate/", views.yourRealEstate, name="your_real_estate"),
    path("zip/", views.real_estate_zip, name="real_estate_zip"),
    path("street/", views.real_estate_street, name="real_estate_street"),
    path("size/", views.real_estate_size, name="real_estate_size"),
    path("price/", views.real_estate_price, name="real_estate_price"),
    path("city/", views.real_estate_city, name="real_estate_city"),
    path("bathrooms/", views.real_estate_bathrooms, name="real_estate_bathrooms"),
    path("bedrooms/", views.real_estate_bedrooms, name="real_estate_bedrooms"),
]
