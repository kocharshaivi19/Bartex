# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-09 01:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BarterSystem', '0003_auto_20170508_1937'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='posted_by_uid',
            new_name='posted_by_uid_id',
        ),
    ]