from django import forms

from .models import Project, Task, ToDo
from account.models import CustomUser

class CreateProjectForm(forms.ModelForm):

    deadline_datetime = forms.SplitDateTimeField(
        label="締め切り日時",
        widget=forms.SplitDateTimeWidget(
            date_attrs={"type":"date"},
            time_attrs={"type":"time"}
        )
    )

    
    contractor_user = forms.ModelChoiceField(
        CustomUser.objects,
        to_field_name='username',
        label='受注者のユーザーID',
        empty_label='入力してください',
        widget=forms.TextInput,
        error_messages={'invalid_choice':'このユーザーID存在しません'}
    )
    supporter = forms.CharField(
        label="あなたのサポーター",
        max_length=255,
        required=False
    )

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
            # "orderer_users",
            # "contractor_users",
            "supporter",
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

    def clean_supporter(self):
        supporter = self.cleaned_data.get("supporter")
        supporters_list = supporter.split(",")
        return supporters_list



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




class ProjectProposeForm(forms.ModelForm):
    c_supporter = forms.CharField(
        label="あなたのサポーター",
        max_length=255,
        required=False
    )
    class Meta:
        model = Project
        fields = [
            "is_accepted",
            "c_supporter",
        ]

    def clean_c_supporter(self):
        c_supporter = self.cleaned_data.get("c_supporter")
        c_supporters_list = c_supporter.split(",")
        return c_supporters_list







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