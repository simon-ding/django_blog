# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 06:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(editable=False, verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='post',
            name='html',
            field=models.TextField(editable=False, verbose_name='html text'),
        ),
    ]
