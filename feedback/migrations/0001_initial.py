# Generated by Django 4.2.7 on 2023-12-06 01:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='コメント')),
                ('posted_at', models.DateTimeField(auto_now_add=True, verbose_name='投稿日')),
                ('self_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedback.feedback', verbose_name='自分自身のid')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='project.task', verbose_name='関連するタスクid')),
            ],
        ),
    ]
