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
    # is_read = models.BooleanField(
    #     default=False,
    #     help_text="既読はTrue"
    # )


# class FeedBackRule(models.Model):

    

#     class Meta:
#         verbose_name = _("FeedBackRule")
#         verbose_name_plural = _("FeedBackRules")

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse("FeedBackRule_detail", kwargs={"pk": self.pk})
