from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = "account"

urlpatterns = [
    path(
        "signup/",
        views.SignUpView.as_view(),
        name="signup"
    ),
    path(
        "signup-success/",
        views.SignUpSuccessView.as_view(),
        name="signup_success"
    ),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="login.html"),
        name="login"
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="logout.html"),
        name="logout"
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="logout.html"),
        name="logout"
    ),
    path(
        "profile/",
        views.UserDetailCreate.as_view(),
        name="create_feedback_rule"
    ),
    
]