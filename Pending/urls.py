
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="pending_index"),
]