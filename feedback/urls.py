from django.urls import path

from . import views

app_name = "feedback"

urlpatterns = [
    path('add-feedback/<int:task_id>', views.FeedbackCreateView.as_view(), name="feedback_add"),
    path('reply/<int:task_id>/<int:feedback_id>', views.FeedbackReplyView.as_view(), name="reply"),
    path('help/<int:pk>', views.HelpView.as_view(), name="help"),
]
