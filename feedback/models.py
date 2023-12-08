from django.db import models

from account.models import CustomUser
from project.models import Project, Task, ToDo


class Feedback(models.Model):
    comment = models.TextField(
        verbose_name="コメント"
    )

    posted_at = models.DateTimeField(
        verbose_name="投稿日",
        auto_now_add=True,
    )
    self = models.ForeignKey(
        "self",
        verbose_name="自分自身のid",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    task = models.ForeignKey(
        Task,
        verbose_name="関連するタスクid",
        on_delete=models.PROTECT,
    )
    user = models.ForeignKey(
        CustomUser,
        verbose_name="投稿者",
        on_delete=models.CASCADE,
    )
