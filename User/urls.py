from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views
from User.forms.login_form import LoginForm


# url: /user/
urlpatterns = [

    # /user/register/
    path("register/", views.register, name="register"),

    # /user/history/
    path("history/", views.user_history, name="user_history"),

    # /user/delete_history/
    path("delete_history/", views.delete_history, name="delete_history"),

    # /user/logout/
    path("logout/", LogoutView.as_view(next_page='login'), name="logout"),

    # /user/profile/
    path("profile", views.profile_update, name="profile"),

    # /user/login/
    path(
        'login/', LoginView.as_view( template_name="User/login.html", authentication_form=LoginForm),
        name='login')
    ]
