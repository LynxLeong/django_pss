# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-22 13:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prs', '0002_auto_20170413_1441'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reportedcases',
            name='case_id',
        ),
        migrations.RemoveField(
            model_name='reportedcases',
            name='case_user',
        ),
    ]
