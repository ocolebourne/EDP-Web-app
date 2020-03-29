# Generated by Django 2.1.5 on 2020-03-26 14:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20200326_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalproject',
            name='user',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='structuredproject',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 26, 14, 57, 26, 753858), verbose_name='date published'),
        ),
    ]
