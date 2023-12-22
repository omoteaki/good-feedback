
# from django.forms import ModelForm, Textarea
from django import forms
from .models import Project, Task, ToDo

class CreateProjectForm(forms.ModelForm):
    # date = forms.DateField(label="日にち")
    # time = forms.TimeField(label="時間")
    # deadline_datetime = forms.SplitDateTimeField(required=False)
    deadline_datetime = forms.SplitDateTimeField()
    # widgets = {
    #     'date': forms.NumberInput(attrs={
    #         "type": "date"
    #     }),
    #     'time': forms.NumberInput(attrs={
    #         "type": "time"
    #     })
    # }
    class Meta:
        model = Project
        fields = [
            "title",
            "about",
            "deadline_datetime",
            "purpose",
            # "time",
            # "date",

            # "created_at",
            # "updated_at",
            # "orderer_user",
            "contractor_user",
            "orderer_users",
            # "contractor_users",
            "reference_image1",
            "reference_image2",
            "reference_image3",
            "reference_movie1",
            "reference_movie2",
            "reference_movie3",
            "reference_music1",
            "reference_music2",
            "reference_music3",
            "reference_url1",
            "reference_url2",
            "reference_url3",
        ]

        # widgets = {
        #     'deadline_datetime': forms.Textarea
        # }


        widgets = {
            "deadline_datetime": forms.widgets.SplitDateTimeWidget
            # "deadline_datetime": forms.widgets.SelectDateWidget
        }



class UpdateProjectForm(forms.ModelForm):
    date = forms.DateField(label="日にち", initial="2023/12/24")
    time = forms.TimeField(label="時間", initial="12:00")
    deadline_datetime = forms.DateTimeField(required=False)

    

    class Meta:
        model = Project
        fields = [
            "title",
            "about",
            "deadline_datetime",
            "time",
            "date",
            # "reference_image1",
            # "reference_image2",
            # "reference_image3",
            # "reference_movie1",
            # "reference_movie2",
            # "reference_movie3",
            # "reference_music1",
            # "reference_music2",
            # "reference_music3",
            # "reference_url1",
            # "reference_url2",
            # "reference_url3",
            # # "created_at",
            # # "updated_at",
            # # "orderer_user",
            # "contractor_user",
            # "orderer_users",
            # # "contractor_users",

        ]

        # widgets = {
        #     'deadline_datetime': forms.Textarea
        # }


        # widgets = {
        #     "deadline_datetime": forms.widgets.SplitDateTimeWidget
        # }



class ProjectProposeForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            "is_accepted",
            "contractor_users",
        ]







class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = (
            'project',
            "updated_at",
        )

class ToDoCreateForm(forms.ModelForm):
    class Meta:
        model = ToDo
        # fields = "__all__"
        exclude = ("project", "task")