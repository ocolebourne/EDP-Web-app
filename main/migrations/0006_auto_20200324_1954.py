# Generated by Django 2.1.5 on 2020-03-24 19:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200324_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='structuredproject',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 24, 19, 54, 23, 604527), verbose_name='date published'),
        ),
    ]
