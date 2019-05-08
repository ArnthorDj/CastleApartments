from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path("register", views.index, name="user_register_index"),
    path("login", LoginView.as_view(template_engine="User/login.html"), name="user_login_index"),
    path("logout", LogoutView.as_view(next_page='login'), name="user_logout_index"),
]