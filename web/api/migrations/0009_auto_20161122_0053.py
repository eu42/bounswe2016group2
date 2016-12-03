# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-22 00:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20161122_0047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='photo',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='value',
            field=models.FloatField(blank=True, null=True),
        ),
    ]