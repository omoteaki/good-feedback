from django.shortcuts import render

from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Max

from .models import Feedback
from .forms import FeedbackForm

from project.models import Task

class FeedbackCreateView(CreateView):
    template_name = "add_feedback.html"
    form_class = FeedbackForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task"] = Task.objects.get(id=self.kwargs["task_id"])
        print(context["task"].project)
        return context

    def get_success_url(self):
        return reverse_lazy("project:project_detail", kwargs={"pk": self.object.task.project.pk})

    

    def form_valid(self, form):
        feedback = form.save(commit=False)
        feedback.user = self.request.user
        feedback.task_id = self.kwargs["task_id"]
        feedback.save()
        return super().form_valid(form)
    

class FeedbackReplyView(CreateView):
    template_name = "add_feedback.html"
    form_class = FeedbackForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reply_to"] = Feedback.objects.get(id=self.kwargs["feedback_id"])
        context["task"] = Task.objects.get(id=self.kwargs["task_id"])

        return context
    

    def get_success_url(self):
        return reverse_lazy("project:project_detail", kwargs={"pk": self.object.task.project.pk})
    
    

    def form_valid(self, form):
        feedback = form.save(commit=False)

        feedback.user = self.request.user
        feedback.task_id = self.kwargs["task_id"]
        feedback.self_id = self.kwargs["feedback_id"]
        feedback.save()
        return super().form_valid(form)
    


class HelpView(DetailView):
    template_name = "help.html"
    model = Feedback


