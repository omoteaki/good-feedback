from django.db import models
import mido
import os
import json
from django.core.files.storage import default_storage
from django.conf import settings

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
    file = models.FileField(
        verbose_name="現状のファイル",
        upload_to="references",
        blank=True,
        null=True,
    )
    midi = models.FileField(
        verbose_name="midiファイル",
        upload_to="references",
        blank=True,
        null=True,
    )

    # midiのマーカー情報を返す
    def marker_of_midi(self):
        file_path = os.path.join(settings.MEDIA_ROOT, str(self.midi))
        
        # ファイルを開いてmidファイルを読み込む
        with open(file_path, 'rb') as midi_file:
            smf = mido.MidiFile(file=midi_file)

            marker_list = []

            for tr in smf.tracks[0]:
                msg = tr.dict()
                if msg["type"] == "marker":
                    time = msg["time"]
                    marker = msg["text"]
                    marker_list.append({"marker":marker, "time":time})

            sum = 0
            for li in marker_list:
                sum += li["time"]
                second = sum / 29120
                li.update(time=second)

            json_list = json.dumps(marker_list)

        return json_list


# class FeedBackRule(models.Model):

    

#     class Meta:
#         verbose_name = _("FeedBackRule")
#         verbose_name_plural = _("FeedBackRules")

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse("FeedBackRule_detail", kwargs={"pk": self.pk})
