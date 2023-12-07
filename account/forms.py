from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm





from .models import CustomUser, UserDetail

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2")

class UserDetailForm(ModelForm):
    class Meta:
        model = UserDetail
        fields = "__all__"