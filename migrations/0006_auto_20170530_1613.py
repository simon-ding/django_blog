# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 08:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 30, 8, 13, 7, 806045, tzinfo=utc), editable=False),
        ),
    ]
