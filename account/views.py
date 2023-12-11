from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm, UserDetailForm
from .models import CustomUser, UserDetail

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
    success_url = reverse_lazy("project:index")

    # def form_valid(self, form):
    #     detail = form.save(commit=False)
    #     detail.user = self.request.user
    #     detail.save()
    #     user_detail1 = CustomUser.save(commit=False)
    #     user_detail1.detail1 = UserDetail.objects.get()
    #     return super().form_valid(form)