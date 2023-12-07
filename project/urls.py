from django.urls import path

from . import views

app_name = "project"

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('new-project-create/', views.CreateProjectView.as_view(), name="create_project"),
    path('project-list/', views.ProjectListView.as_view(), name="project_list"),
    path('project/<int:pk>', views.ProjectDetailView.as_view(), name="project_detail"),
    path('new-project/<int:created_user_id>', views.CreateProjectSuccessView.as_view(), name="create_project_done"),
    path('add-task/<int:id>', views.AddTaskView.as_view(), name="add_task"),
    path('task-list/<int:id>', views.TaskListView.as_view(), name="task_list"),
    path('task-detail/<int:pk>', views.TaskDetailView.as_view(), name="task_detail"),
    path('task-edit/<int:pk>', views.TaskEditView.as_view(), name="task_edit"),
    path('task-delete/<int:pk>', views.TaskDeleteView.as_view(), name="task_delete"),


    path('mypage', views.MypageView.as_view(), name="mypage"),
    path('about', views.AboutUsView.as_view(), name="about_us"),
]
