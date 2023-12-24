from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm





from .models import CustomUser, UserDetail

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "last_name", "first_name", "email", "password1", "password2")
        # fields = "__all__"
        # lastnameは苗字

class UserDetailForm(ModelForm):
    class Meta:
        model = UserDetail
        fields = (
            "label_select",
            "profile",
            "rule",
            "convenient_time_from",
            "convenient_time_to",
            "how_to_contact",
        )
