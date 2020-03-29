# Generated by Django 2.1.5 on 2020-03-26 15:06

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20200326_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalproject',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='structuredproject',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 26, 15, 6, 57, 336036), verbose_name='date published'),
        ),
    ]
