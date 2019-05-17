from django.urls import path
from . import views

# url: /real_estate/
urlpatterns = [
    # /real_estate/
    path("", views.index, name="real_estate"),
    # /real_estate/info/:id/
    path("info/<int:id>", views.get_real_estate_by_id, name="real_estate_information"),
    # /real_estate/pay/:id/
    path("pay/<int:id>", views.payment_information, name="payment_information_index"),
    # /real_estate/pay/:id/confirmation/
    path("pay/<int:id>/confirmation/", views.payment_confirmation, name="payment_confirmation"),
    # /real_estate/pay/id/bought/
    path("pay/<int:id>/bought/", views.bought_real_estate, name="bought"),
    # /real_estate/add/
    path("add/", views.add_real_estate, name="add_real_estate_index"),
    # /real_estate/update/:id/
    path("update/<int:id>", views.update_real_estate, name="update_real_estate_index"),
    # /real_estate/add_images/id/
    path("add_images/<int:id>", views.add_real_estate_images, name="real_estate_image"),
    # /real_estate/zip/
    path("zip/", views.real_estate_zip, name="real_estate_zip"),
    # /real_estate/street/
    path("street/", views.real_estate_street, name="real_estate_street"),
    # /real_estate/size/
    path("size/", views.real_estate_size, name="real_estate_size"),
    # /real_estate/price/
    path("price/", views.real_estate_price, name="real_estate_price"),
    # /real_estate/city/
    path("city/", views.real_estate_city, name="real_estate_city"),
    # /real_estate/bathrooms
    path("bathrooms/", views.real_estate_bathrooms, name="real_estate_bathrooms"),
    # /real_estate/bedrooms
    path("bedrooms/", views.real_estate_bedrooms, name="real_estate_bedrooms"),
]
