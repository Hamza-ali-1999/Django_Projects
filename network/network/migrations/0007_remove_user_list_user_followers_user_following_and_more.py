# Generated by Django 4.1 on 2023-07-11 20:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0006_user_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='list',
        ),
        migrations.AddField(
            model_name='user',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='follower_list', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='following_list', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='FollowingList',
        ),
    ]
