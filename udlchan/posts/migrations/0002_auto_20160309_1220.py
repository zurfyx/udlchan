# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-09 12:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Post', verbose_name='Category'),
        ),
    ]
