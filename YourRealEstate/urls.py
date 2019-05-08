
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="your_real_estate_index"),
]