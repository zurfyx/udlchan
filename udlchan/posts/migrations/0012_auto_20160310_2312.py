# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-10 23:12
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_remove_post_vote'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='post',
            managers=[
                ('vote', django.db.models.manager.Manager()),
            ],
        ),
    ]
