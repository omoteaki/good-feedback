from django.urls import path

from . import views

app_name = "feedback"

urlpatterns = [
    path('add-feedback/<int:task_id>/<int:project_id>', views.FeedbackCreateView.as_view(), name="feedback_add"),
]
