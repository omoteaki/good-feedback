# Generated by Django 4.2.7 on 2023-12-07 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_project_created_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='content',
            field=models.TextField(verbose_name='本文'),
        ),
    ]
