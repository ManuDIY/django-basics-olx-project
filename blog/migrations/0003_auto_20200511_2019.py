# Generated by Django 3.0.6 on 2020-05-11 20:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_title2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title2',
        ),
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
