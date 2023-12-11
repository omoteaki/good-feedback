from django.db import models

from account.models import CustomUser

class Project(models.Model):
    title = models.CharField(
        verbose_name="プロジェクトのタイトル",
        max_length=30,
    )
    about = models.TextField(
        verbose_name="このプロジェクトについて"
    )
    deadline_datetime = models.DateTimeField(
        verbose_name="締め切り日時",
        # auto_now_add=False  # ここないからエラーの可能性
    )
    reference_image1 = models.ImageField(
        verbose_name="参考画像1",
        upload_to="references",
        blank=True,
        null=True,
    )
    reference_image2 = models.ImageField(
        verbose_name="参考画像2",
        upload_to="references",
        blank=True,
        null=True,
    )
    reference_image3 = models.ImageField(
        verbose_name="参考画像3",
        upload_to="references",
        blank=True,
        null=True,
    )
    reference_movie1 = models.FileField(
        verbose_name="参考動画1",
        upload_to="references",
        blank=True,
        null=True,
    )
    reference_movie2 = models.FileField(
        verbose_name="参考動画2",
        upload_to="references",
        blank=True,
        null=True,
    )
    reference_movie3 = models.FileField(
        verbose_name="参考動画3",
        upload_to="references",
        blank=True,
        null=True,
    )
    reference_music1 = models.FileField(
        verbose_name="参考音源1",
        upload_to="references",
        blank=True,
        null=True,
    )
    reference_music2 = models.FileField(
        verbose_name="参考音源2",
        upload_to="references",
        blank=True,
        null=True,
    )
    reference_music3 = models.FileField(
        verbose_name="参考音源3",
        upload_to="references",
        blank=True,
        null=True,
    )
    reference_url1 = models.URLField(
        verbose_name="参考URL1",
        blank=True,
        null=True,
    )
    reference_url2 = models.URLField(
        verbose_name="参考URL2",
        blank=True,
        null=True,
    )
    reference_url3 = models.URLField(
        verbose_name="参考URL3",
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(
        verbose_name="プロジェクトを登録した日時",
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name="プロジェクトの詳細を更新した時間",
        auto_now=True,
    )
    orderer_user = models.ForeignKey(
        CustomUser,
        verbose_name="発注者",
        on_delete=models.PROTECT,
        related_name="orderer_user",
    )
    contractor_user = models.ForeignKey(
        CustomUser,
        verbose_name="受注者",
        on_delete=models.PROTECT,
        related_name="contractor_user",
        
    )
    orderer_users = models.ManyToManyField(
        CustomUser,
        verbose_name="発注者のサポーター",
        blank=True,
        related_name="orderer_users",
    )
    contractor_users = models.ManyToManyField(
        CustomUser,
        verbose_name="受注者のサポーター",
        blank=True,
        related_name="contractor_users",
    )
    created_user = models.ForeignKey(
        CustomUser,
        verbose_name="プロジェクトの作成者",
        on_delete=models.PROTECT,
        related_name="created_user"
    )

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(
        verbose_name="タイトル",
        max_length=30,
    )
    content = models.TextField(
        verbose_name="本文"
    )
    deadline_datetime = models.DateTimeField(
        verbose_name="締め切り日時",
        # auto_now_add=False  # 書いていないからエラー出るかも
    )
    added_at = models.DateTimeField(
        verbose_name="タスクを追加した日時",
        auto_now_add=True,
    )
    project = models.ForeignKey(
        Project,
        verbose_name="プロジェクト",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title
    

class ToDo(models.Model):
    title = models.CharField(
        verbose_name="ToDoのタイトル",
        max_length=100

    )
    added_at = models.DateTimeField(
        verbose_name="ToDoを追加した日時",
        auto_now_add=True,
    )
    task = models.ForeignKey(
        Task,
        verbose_name="関連するタスク",
        on_delete=models.CASCADE,
    )
    is_done = models.BooleanField(
        default=False,
        help_text="todoを完了させたらTrue"
    )
    project = models.ForeignKey(
        Project,
        verbose_name="関連するプロジェクト",
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.title