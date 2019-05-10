
from django.urls import path
from . import views

urlpatterns = [
    path("", views.your_real_estate, name="your_real_estate_index"),
    path("add/", views.add_real_estate, name="add_real_estate_index"),
    path("add/confirmation/", views.add_real_estate_confirmation, name="add_real_estate_confirmation_index")
]