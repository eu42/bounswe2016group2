# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-22 00:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20161121_2346'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='photo',
            field=models.URLField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='photo',
            field=models.URLField(max_length=255, null=True),
        ),
    ]