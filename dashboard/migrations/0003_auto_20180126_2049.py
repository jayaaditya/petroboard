# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-26 20:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20180126_2047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='customer',
        ),
    ]
