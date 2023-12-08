from django.shortcuts import render

from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Max

from .models import Feedback
from .forms import FeedbackForm

class FeedbackCreateView(CreateView):
    template_name = "add_feedback.html"
    form_class = FeedbackForm

    def get_success_url(self):
        return reverse_lazy("project:project_detail", kwargs={"pk": self.kwargs["project_id"]})
    

    def form_valid(self, form):
        feedback = form.save(commit=False)

        feedback.user = self.request.user
        feedback.task_id = self.kwargs["task_id"]
        feedback.save()
        return super().form_valid(form)
    
