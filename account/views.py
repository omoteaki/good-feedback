from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm, UserDetailForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "signup.html"
    success_url = reverse_lazy("account:signup_success")

    def form_valid(self, form):
        user = form.save()
        self.object = user
        return super().form_valid(form)

class SignUpSuccessView(TemplateView):
    template_name = "signup_success.html"


class UserDetailCreate(CreateView):
    form_class = UserDetailForm
    template_name = "create_feedback_rule.html"
    success_url = reverse_lazy("project:mypage")

    def form_valid(self, form):
        detail = form.save()
        self.object = detail
        return super().form_valid(form)