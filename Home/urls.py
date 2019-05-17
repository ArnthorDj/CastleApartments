from django.urls import path
from . import views

# url: /home/
urlpatterns = [
    # /home/
    path("", views.index, name="home_index"),
]
