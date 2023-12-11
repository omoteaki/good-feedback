from django.db import models
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
    pass
    # detail1 = models.ForeignKey(
    #     UserDetail,
    #     verbose_name="お仕事プロフィール1(デフォルト)",
    #     on_delete=models.PROTECT,
    #     related_name="detail1",
    #     blank=True,
    #     null=True,
    # )
    # detail2 = models.ForeignKey(
    #     UserDetail,
    #     verbose_name="お仕事プロフィール2",
    #     on_delete=models.PROTECT,
    #     blank=True,
    #     null=True,
    #     related_name="detail2",
    # )
    # detail3 = models.ForeignKey(
    #     UserDetail,
    #     verbose_name="お仕事プロフィール3",
    #     on_delete=models.PROTECT,
    #     blank=True,
    #     null=True,
    #     related_name="detail3",
    # )

class UserDetail(models.Model):
    profile = models.TextField(
        verbose_name="仕事内容"
    )
    rule = models.TextField(
        verbose_name="仕事の進め方やお願い"
    )
    convenient_time_from = models.TimeField(
        verbose_name="都合の良い時間帯の開始時刻",
        # auto_now_add=False  # ここないからエラー出るかも？
    )
    convenient_time_to = models.TimeField(
        verbose_name="都合の良い時間帯の終了時刻",
        # auto_now_add=False  # ここないからエラー出るかも？
    )

    CONTACT = (
        ("tel", "電話"),
        ("mail", "メール"),
        ("line", "ライン"),
        ("skype", "スカイプ"),
    )

    how_to_contact = models.CharField(
        verbose_name="連絡手段",
        max_length=50,
        choices=CONTACT
    )
    user = models.ForeignKey(
        CustomUser,
        verbose_name="ユーザー",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    LABEL = (
        ("detail1", "プロフィール1(デフォルト)"),
        ("detail2", "プロフィール2"),
        ("detail3", "プロフィール3"),

    )

    label_select = models.CharField(
        verbose_name="ラベル",
        max_length=50,
        choices=LABEL
    )
