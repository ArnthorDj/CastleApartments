from django.urls import path
from . import views

# url: /employees/
urlpatterns = [
    path("", views.index, name='employees_index'),
]
