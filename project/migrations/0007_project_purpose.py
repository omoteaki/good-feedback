# Generated by Django 4.2.7 on 2023-12-16 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_project_feedback_rule_project_is_accepted'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='purpose',
            field=models.TextField(null=True, verbose_name='このプロジェクトで実現したいこと'),
        ),
    ]