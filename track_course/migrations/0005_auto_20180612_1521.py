# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-12 15:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track_course', '0004_auto_20180606_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trackcourse',
            name='detail',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
