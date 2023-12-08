# Generated by Django 4.2.7 on 2023-12-08 02:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feedback', '0002_alter_feedback_self_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='self_id',
            new_name='self',
        ),
        migrations.AddField(
            model_name='feedback',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='投稿者'),
            preserve_default=False,
        ),
    ]