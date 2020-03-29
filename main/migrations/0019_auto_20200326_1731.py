# Generated by Django 2.1.5 on 2020-03-26 17:31

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20200326_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalproject',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='structuredproject',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 26, 17, 31, 56, 311109), verbose_name='date published'),
        ),
    ]
