# Generated by Django 4.1 on 2022-08-28 02:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_remove_auction_item_tags_auction_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='time_of_creation',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 27, 22, 15, 50, 50817)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='time_of_commment',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 27, 22, 15, 50, 50817)),
        ),
    ]
