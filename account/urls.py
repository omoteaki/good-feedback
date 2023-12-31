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
        "user-data/<int:pk>",
        views.UserUpdate.as_view(),
        name="user_update"
    ),
    path(
        "profile/",
        views.UserDetailCreate.as_view(),
        name="create_feedback_rule"
    ),
    path(
        "profile/<int:detail_num>",
        views.UserDetailCreate.as_view(),
        name="create_feedback_rule"
    ),
    path(
        "profile-edit/<int:pk>",
        views.UserDetailUpdate.as_view(),
        name="update_feedback_rule"
    ),
    path(
        "mypage/<int:pk>",
        views.CustomUserDetailView.as_view(),
        name="mypage"
    ),
    
]