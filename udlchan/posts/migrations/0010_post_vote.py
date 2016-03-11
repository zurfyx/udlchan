# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-10 17:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0001_initial'),
        ('posts', '0009_remove_post_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='vote',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='votes.Vote'),
            preserve_default=False,
        ),
    ]
