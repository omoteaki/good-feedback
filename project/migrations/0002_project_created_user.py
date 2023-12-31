# Generated by Django 4.2.7 on 2023-12-06 05:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='created_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='created_user', to=settings.AUTH_USER_MODEL, verbose_name='プロジェクトの作成者'),
            preserve_default=False,
        ),
    ]
