from django.shortcuts import render

from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Max

from .models import Project, Task, ToDo
from .forms import CreateProjectForm, AddTaskForm, ToDoCreateForm

class IndexView(TemplateView):
    template_name = "index.html"


class AboutUsView(TemplateView):
    template_name = "about_us.html"


@method_decorator(login_required, name="dispatch")
class CreateProjectView(CreateView):
    form_class = CreateProjectForm
    template_name = "create_project.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["created_user_id"] = self.request.user
        return context
    
    def get_success_url(self):
        return reverse_lazy("project:create_project_done", kwargs={"created_user_id": self.request.user.id})

    def form_valid(self, form):
        new_project = form.save(commit=False)
        new_project.created_user = self.request.user
        new_project.save()
        # create_user_id

        return super().form_valid(form)

class CreateProjectSuccessView(ListView):
    template_name = "new_project.html"
    # model = Project

    def get_queryset(self):
        print(self.request.user)
        new_project_id = Project.objects.filter(created_user = self.kwargs["created_user_id"]).aggregate(Max("id"))
        new_project = Project.objects.get(id=new_project_id["id__max"])
        return new_project
    

class ProjectListView(ListView):
    template_name = "project_list.html"
    def get_queryset(self):
        projects = Project.objects.filter(created_user= self.request.user)
        return projects
    

class ProjectDetailView(ListView):
    template_name = "project_detail.html"

    def get_queryset(self):
        project = Project.objects.get(id=self.kwargs["pk"])
        tasks = Task.objects.filter(project_id=self.kwargs["pk"])
        return (project, tasks)
    




# タスク追加関連
class AddTaskView(CreateView):
    form_class = AddTaskForm
    template_name = "add_task.html"
    success_url = reverse_lazy("project:task_list")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        print(self.kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy("project:task_list", kwargs={"id": self.kwargs["id"]})

    def form_valid(self, form):
        new_task = form.save(commit=False)
        new_task.project_id = self.kwargs["id"]
        new_task.save()
        # self.object = new_task
        return super().form_valid(form)
    

class TaskListView(ListView):
    template_name = "task_list.html"

    def get_queryset(self):
        Tasks = Task.objects.filter(project_id=self.kwargs["id"])
        return Tasks


class TaskDetailView(DetailView):
    template_name = "task_detail.html"
    model = Task

class TaskEditView(UpdateView):
    template_name = "task_edit.html"
    model = Task
    fields = [
        "title",
        "content",
        "deadline_datetime",
        #更新日必要じゃない？？
    ]

    def get_success_url(self):
        return reverse_lazy("project:task_detail", kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        new_task = form.save(commit=False)
        new_task.save()
        # self.object = new_task
        return super().form_valid(form)
    
class TaskDeleteView(DeleteView):
    model = Task
    template_name = "task_delete.html"
    success_url = reverse_lazy("project:index")

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    

# ToDo
# class ToDoCreateView(CreateView):
#     form_class = ToDoCreateForm
#     template_name = "add_todo.html"

#     def get_success_url(self):
#         return reverse_lazy("project:task_list", kwargs={"id": self.kwargs["id"]})

#     def form_valid(self, form):
#         new_task = form.save(commit=False)
#         new_task.project_id = self.kwargs["id"]
#         new_task.save()
#         # self.object = new_task
#         return super().form_valid(form)



class MypageView(ListView):
    template_name = "mypage.html"

    def get_queryset(self):
        request_user_projects = Project.objects.filter(created_user=self.request.user)
        return request_user_projects
    