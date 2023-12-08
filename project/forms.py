
# from django.forms import ModelForm, Textarea
from django import forms
from .models import Project, Task, ToDo

class CreateProjectForm(forms.ModelForm):
    date = forms.DateField
    time = forms.TimeField

    class Meta:
        model = Project
        fields = "__all__"
        # fields += ("time", "")
        # fields = exclude
        # print(fields)
        # fields = [
        #     "title",
        #     "about",
        #     "deadline_datetime",
        #     "reference_image1",
        #     "reference_image2",
        #     "reference_image3",
        #     "reference_movie1",
        #     "reference_movie2",
        #     "reference_movie3",
        #     "reference_music1",
        #     "reference_music2",
        #     "reference_music3",
        #     "reference_url1",
        #     "reference_url2",
        #     "reference_url3",
        #     # "created_at",
        #     # "updated_at",
        #     "orderer_user",
        #     "contractor_user",
        #     "orderer_users",
        #     "contractor_users",
        #     "time",
        #     "date",
        # ]

        # widgets = {
        #     'deadline_datetime': forms.Textarea
        # }
        # widgets = {
        #     'date': forms.NumberInput(attrs={
        #         "type": "date"
        #     }),
        #     'time': forms.NumberInput(attrs={
        #         "type": "time"
        #     })
        # }

        # widgets = {
        #     "deadline_datetime": forms.widgets.SplitDateTimeWidget
        # }



class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ('project',)

class ToDoCreateForm(forms.ModelForm):
    class Meta:
        model = ToDo
        # fields = "__all__"
        exclude = ("project", "task")