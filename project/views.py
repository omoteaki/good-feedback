from typing import Any


from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect


from datetime import date, time, datetime, timedelta
from django.utils.timezone import make_aware
# from backports.zoneinfo import ZoneInfo
from zoneinfo import ZoneInfo

from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Max, Min, Avg
from django.db.models import Q, F

from .models import Project, Task, ToDo
from feedback.models import Feedback
from account.models import UserDetail, CustomUser
from .forms import CreateProjectForm, AddTaskForm, ToDoCreateForm, UpdateProjectForm, ProjectProposeForm



# ログインしていなかったらindex、ログインユーザーならマイページ
class IndexView(ListView):
    template_name = "index.html"

    def get_queryset(self):
        if  self.request.user.is_authenticated:
            request_user_projects = Project.objects.filter( Q(created_user=self.request.user)|Q(orderer_user=self.request.user)|Q(contractor_user=self.request.user)).exclude(is_done=True).filter(is_accepted=True).annotate(delta=F("deadline_datetime") - make_aware(datetime.now())).order_by("deadline_datetime")
            return request_user_projects
        else:
            pass

    def get_context_data(self, **kwargs):
        if  self.request.user.is_authenticated:
            context = super().get_context_data(**kwargs)
            context["myproject"] = True
            context["closed_project"] = Project.objects.filter( Q(created_user=self.request.user)|Q(orderer_user=self.request.user)|Q(contractor_user=self.request.user)).filter(is_done=True)
            context["ordered_project_list"] = Project.objects.filter(contractor_user=self.request.user).filter(is_accepted=False)
            context["order_project_list"] = Project.objects.filter(orderer_user=self.request.user).filter(is_accepted=False)


            for object in context["object_list"]:
                print(type(object.delta))
                txt = str(object.delta)
                pos = txt.find(' day')
                # print(pos)
                if pos >= 1:
                    object.int_delta = int(txt[:pos])
                else:
                    object.int_delta = 0

            context["near_deadline_objects"] = context["object_list"].filter(delta__lte=timedelta(weeks=1))

            return context
        else:
            pass


class AboutUsView(TemplateView):
    template_name = "about_us.html"


class ProposeProjectView(UpdateView):
    form_class = ProjectProposeForm
    template_name = "propose_project.html"
    model = Project
    context_object_name = "project"

    def get_success_url(self):
        return reverse_lazy("project:feedback_set", kwargs={"pk": self.kwargs["pk"]})

    def form_valid(self, form):
        project = form.save(commit=False)
        c_supporters_list = form.cleaned_data.get("c_supporter")

        project.save()
        if c_supporters_list:
            for c_supporter in c_supporters_list:
                project.contractor_users.add(CustomUser.objects.get(username=c_supporter))

        form.save_m2m()

        return super().form_valid(form)

class SetFeedbackView(UpdateView):
    model = Project
    template_name = "set_feedback.html"
    fields = [
        "feedback_rule"
    ]

    def get_success_url(self):
        return reverse_lazy("project:project_detail", kwargs={"pk": self.kwargs["pk"]})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_detail_list"] = UserDetail.objects.filter(user_id=self.request.user)
        print(context["user_detail_list"])
        print(context["form"].fields["feedback_rule"].queryset)
        context["form"].fields["feedback_rule"].queryset = UserDetail.objects.filter(user=self.request.user)
        print(context["form"].fields["feedback_rule"].queryset)
        if not 'propose_message' in self.request.session:
            self.request.session['propose_message'] = "warning"
        return context
    
    def form_valid(self, form):
        detail_set = form.save(commit=False)
        detail_set.save()
        if 'propose_message' in self.request.session:
            self.request.session['propose_message'] = "success"
        return super().form_valid(form)
    




@method_decorator(login_required, name="dispatch")
class CreateProjectView(CreateView):
    form_class = CreateProjectForm
    template_name = "create_project.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["created_user_id"] = self.request.user
        return context
    
    def get_success_url(self):
        return reverse_lazy("project:create_project_done", kwargs={"pk": self.object.pk})

    def form_valid(self, form):

        new_project = form.save(commit=False)
        supporters_list = form.cleaned_data.get("supporter")
        new_project.created_user = self.request.user
        new_project.orderer_user = self.request.user
        print(supporters_list)
        new_project.save()

        if supporters_list:
            for supporter in supporters_list:
                if supporter:
                    new_project.orderer_users.add(CustomUser.objects.get(username=supporter))

        form.save_m2m()



        return super().form_valid(form)


class CreateProjectSuccessView(UpdateView):
    template_name = "new_project.html"
    model = Project
    form_class = CreateProjectForm




class ProjectListView(ListView):
    template_name = "project_list.html"
    def get_queryset(self):
        projects = Project.objects.filter(created_user= self.request.user)
        return projects
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     print(self.object_list)
    #     return context
    

class ProjectDetailView(DetailView):
    template_name = "project_detail.html"
    context_object_name = "project"
    model = Project

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = Task.objects.filter(project_id=self.kwargs["pk"]).annotate(count=Count("feedback"))
        # context["feedbacks"] = Feedback.objects.all()
        # 本当は、projectに紐づいている、taskに紐づいているfeedbackだけ取り出したい
        context["feedbacks"] = Feedback.objects.filter(task_id__in=context["tasks"])
        # for f in context["feedbacks"]:
        # print(list)
        # for li in list:
        #     print(li)

        # for li in list:
        #     print(li)

        context["todo_list"] = ToDo.objects.filter(project_id=self.kwargs["pk"])
        context["detail"] = UserDetail.objects.filter(user_id=self.object.contractor_user)
        # print(context["detail"])
        if 'propose_message' in self.request.session:
            context["message"] = self.request.session['propose_message']
            del self.request.session['propose_message']

        # print(context["project"].contractor_users.all)
        # for us in context["project"].contractor_users.all:
        #     print(us)
        return context
    


# プロジェクトの発注者だけがプロジェクト全体の編集が可能
class ProjectUpdateView(UpdateView):
    template_name = "update_project.html"
    model = Project


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["date"] = self.object.deadline_datetime.date()
        context["time"] = self.object.deadline_datetime.time()
        context["test"] = "hoge"
        print(context["test"])
        return context
    
    # model.time = model.deadline_datetime.time()
    # model.date = model.deadline_datetime.date()
    form_class = UpdateProjectForm
    # fields = [
    #     "title",
    #     "about",
    #     "time",
    #     "date",
    #     "deadline_datetime",  
    # ]


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["created_user_id"] = self.request.user
        return context
    
    def get_success_url(self):
        return reverse_lazy("project:create_project_done", kwargs={"created_user_id": self.request.user.id})

    def form_valid(self, form):
        new_project = form.save(commit=False)
        new_project.deadline_datetime = datetime.combine(form.cleaned_data["date"], form.cleaned_data["time"], tzinfo=ZoneInfo(key='Asia/Tokyo'))

        new_project.save()

        return super().form_valid(form)



class ProjectDoneView(UpdateView):
    template_name = "project_done.html"
    success_url = reverse_lazy("project:project_done_success")

    model = Project
    fields = [
        "is_done",
    ]

    def form_valid(self, form):
        project = form.save(commit=False)
        project.save()
        return super().form_valid(form)
    
class ProjectDoneSuccessView(TemplateView):
    template_name = "project_done_success.html"



# タスク追加関連
class AddTaskView(CreateView):
    form_class = AddTaskForm
    template_name = "add_task.html"
    success_url = reverse_lazy("project:task_list")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["button_message"] = "タスクを追加する"
        context["pk"] = self.kwargs["pk"]
        print(context)
        print(self.kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy("project:task_list", kwargs={"pk": self.kwargs["pk"]})

    def form_valid(self, form):
        new_task = form.save(commit=False)
        new_task.project_id = self.kwargs["pk"]
        new_task.save()
        # self.object = new_task
        return super().form_valid(form)


class TaskListView(ListView):
    template_name = "task_list.html"

    def get_queryset(self):
        Tasks = Task.objects.filter(project_id=self.kwargs["pk"])
        return Tasks

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["project"] = Project.objects.get(id=self.kwargs["pk"])
        return context



class TaskDetailView(DetailView):
    template_name = "task_detail.html"
    model = Task

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["feedbacks"] = Feedback.objects.filter(task_id=self.object)
        context["todos"] = ToDo.objects.filter(task_id=self.object)
        print(context["feedbacks"])
        return context


class TaskEditView(UpdateView):
    template_name = "task_edit.html"
    model = Task
    fields = [
        "title",
        "content",
        "deadline_datetime",
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["button_message"] = "タスクを更新"
        return context
    
    def get_success_url(self):
        return reverse_lazy("project:task_detail", kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        new_task = form.save(commit=False)
        new_task.save()
        return super().form_valid(form)
    
class TaskDeleteView(DeleteView):
    model = Task
    template_name = "task_delete.html"
    success_url = reverse_lazy("project:index")

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    

# ToDo
class ToDoCreateView(CreateView):
    form_class = ToDoCreateForm
    template_name = "add_todo.html"

    def get_success_url(self):
        return reverse_lazy("project:project_detail", kwargs={"pk": self.kwargs["project_id"]})

    def form_valid(self, form):
        new_task = form.save(commit=False)
        new_task.project_id = self.kwargs["project_id"]
        new_task.task_id = self.kwargs["pk"]
        new_task.save()
        print(self.kwargs["pk"])
        # self.object = new_task
        return super().form_valid(form)


# 関数を追加したため、不使用
class ToDoDoneView(UpdateView):
    template_name = "add_todo.html"
    model = ToDo
    fields = [
        "title",
    ]

    def get_success_url(self):
        return reverse_lazy("project:project_detail", kwargs={"pk": self.object.project.id})

    def form_valid(self, form):
        task = form.save(commit=False)
        task.is_done = True
        task.save()
        return super().form_valid(form)
    


def todo_done(request, pk):
    todo = get_object_or_404(ToDo, id=pk)
    project_id = todo.project.pk
    if todo.is_done:
        todo.is_done = False
        todo.save()
    else:
        todo.is_done = True
        todo.save()

    return HttpResponseRedirect(reverse('project:project_detail', kwargs={"pk": project_id}))





# 関数を追加したため、不使用
class ToDoDeleteView(DeleteView):
    model = ToDo
    template_name = "task_delete.html"
    def get_success_url(self):
        return reverse_lazy("project:project_detail", kwargs={"pk": self.object.project.id})

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)




def todo_delete(request, pk):
    todo = get_object_or_404(ToDo, id=pk)
    print(todo)
    project_id = todo.project.pk

    if request.POST:
        todo.delete()

    return HttpResponseRedirect(reverse('project:project_detail', kwargs={"pk": project_id}))


