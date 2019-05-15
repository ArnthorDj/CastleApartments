from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views
from User.forms.login_form import LoginForm


urlpatterns = [
    path("register/", views.register, name="register"),
    path("history/", views.user_history, name="user_history"),
    # path("login/", LoginView.as_view(template_name="User/login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page='login'), name="logout"),
    path("profile", views.profile_update, name="profile"),

    path(
        'login/', LoginView.as_view( template_name="User/login.html", authentication_form=LoginForm),
        name='login')
    ]
