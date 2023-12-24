from django.views.generic import CreateView, TemplateView, DetailView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView


from .forms import CustomUserCreationForm, UserDetailForm
from .models import CustomUser, UserDetail

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "signup.html"
    success_url = reverse_lazy("account:signup_success")

    def form_valid(self, form):
        user = form.save()
        self.object = user
        print(self.object)
        print(self.object.username)
        print(self.request.session)
        if not 'new_user' in self.request.session:
            self.request.session['new_user'] = self.object.username
        print(self.request.session['new_user'])

        return super().form_valid(form)

class SignUpSuccessView(LoginView):
    template_name = "signup_success.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'new_user' in self.request.session:
            print(self.request.session['new_user'])
            context["new_user"] = self.request.session['new_user']
            del self.request.session['new_user']
            print('new_user' in self.request.session)
        else:
            # context["new_user"] = ""
            pass
        


        return context
    


class UserUpdate(UpdateView):
    model = CustomUser
    fields = (
        "username",
        "last_name",
        "first_name",
        "email",
    )

    template_name = "user_update.html"
    success_url = reverse_lazy("project:index")
    
    def get_success_url(self):
        return reverse_lazy("account:mypage", kwargs={"pk": self.request.user.id})


    def form_valid(self, form):
        user_update = form.save(commit=False)
        user_update.user = self.request.user
        user_update.save()
        # user_detail1 = CustomUser.save(commit=False)
        # user_detail1.detail1 = UserDetail.objects.get()
        return super().form_valid(form)


class UserDetailCreate(CreateView):
    form_class = UserDetailForm
    template_name = "create_feedback_rule.html"
    
    def get_success_url(self):
        return reverse_lazy("account:mypage", kwargs={"pk": self.request.user.id})


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["button_message"] = "登録する"
        if "detail_num" in self.kwargs:
            num = self.kwargs["detail_num"]
            str_num = str(num)
            context["detail_num"] = "detail" + str_num
        else:
            pass
        return context
    


    def form_valid(self, form):
        detail = form.save(commit=False)
        detail.user = self.request.user
        detail.save()
        # user_detail1 = CustomUser.save(commit=False)
        # user_detail1.detail1 = UserDetail.objects.get()
        return super().form_valid(form)
    

class UserDetailUpdate(UpdateView):
    model = UserDetail
    form_class = UserDetailForm
    template_name = "create_feedback_rule.html"
    
    def get_success_url(self):
        return reverse_lazy("account:mypage", kwargs={"pk": self.request.user.id})


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["button_message"] = "更新する"
        return context

    def form_valid(self, form):
        detail = form.save(commit=False)
        detail.user = self.request.user
        detail.save()
        for f in form:
            print(f.name)
        # user_detail1 = CustomUser.save(commit=False)
        # user_detail1.detail1 = UserDetail.objects.get()
        return super().form_valid(form)
    



class CustomUserDetailView(DetailView):
    model = CustomUser
    template_name = "mypage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["details"] = UserDetail.objects.filter(user=self.request.user)
        context["mypage"] = True
        print(context["details"])
        return context
    
