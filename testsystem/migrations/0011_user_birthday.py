# Generated by Django 3.0.7 on 2023-04-09 12:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testsystem', '0010_merge_20200808_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2023, 4, 9, 12, 21, 7, 517606), verbose_name='生日'),
        ),
    ]
