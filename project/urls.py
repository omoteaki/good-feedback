from django.urls import path

from . import views

app_name = "project"

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('new-project-create/', views.CreateProjectView.as_view(), name="create_project"),
    path('project-list/', views.ProjectListView.as_view(), name="project_list"),
    path('project/<int:pk>', views.ProjectDetailView.as_view(), name="project_detail"),
    path('new-project/<int:created_user_id>', views.CreateProjectSuccessView.as_view(), name="create_project_done"),
    path('project-update/<int:pk>', views.ProjectUpdateView.as_view(), name="project_update"),
    path('project-done/<int:pk>', views.ProjectDoneView.as_view(), name="project_done"),
    path('project-finish', views.ProjectDoneSuccessView.as_view(), name="project_done_success"),
    path('add-task/<int:id>', views.AddTaskView.as_view(), name="add_task"),
    path('task-list/<int:id>', views.TaskListView.as_view(), name="task_list"),
    path('task-detail/<int:pk>', views.TaskDetailView.as_view(), name="task_detail"),
    path('task-edit/<int:pk>', views.TaskEditView.as_view(), name="task_edit"),
    path('task-delete/<int:pk>', views.TaskDeleteView.as_view(), name="task_delete"),
    path('add-todo/<int:pk>/<int:project_id>', views.ToDoCreateView.as_view(), name="add_todo"),
    path('todo-check/<int:pk>/<int:project_id>', views.ToDoDoneView.as_view(), name="todo_checked"),
    path('todo-delete/<int:pk>', views.ToDoDeleteView.as_view(), name="todo_delete"),


    path('about', views.AboutUsView.as_view(), name="about_us"),
]
