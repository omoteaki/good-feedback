# Generated by Django 4.2.7 on 2023-12-21 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0003_rename_self_id_feedback_self_feedback_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='references', verbose_name='現状のファイル'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='midi',
            field=models.FileField(blank=True, null=True, upload_to='references', verbose_name='midiファイル'),
        ),
    ]