# Generated by Django 4.1 on 2022-09-01 01:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0039_auction_closed_alter_auction_time_of_creation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='time_of_creation',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 31, 21, 40, 15, 190594)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.CharField(default='08/31/2022, 21:40:15', max_length=200),
        ),
    ]
