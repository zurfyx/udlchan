# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-11 09:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0013_auto_20160311_0854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(default='', max_length=300, unique=True),
        ),
    ]
