# Generated by Django 2.1.5 on 2020-03-27 16:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_auto_20200327_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='structuredprojectcontent',
            name='slug',
            field=models.TextField(default='introduction'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='structuredproject',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 27, 16, 31, 53, 484173), verbose_name='date published'),
        ),
    ]
