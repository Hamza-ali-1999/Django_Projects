# Generated by Django 4.1 on 2022-08-26 23:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_alter_auction_latest_bid_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buyer',
            name='bid_item',
        ),
        migrations.AlterField(
            model_name='auction',
            name='time_of_creation',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 26, 19, 38, 33, 604740)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='time_of_commment',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 26, 19, 38, 33, 604740)),
        ),
    ]
