# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-02 13:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('knacks', '0015_auto_20160702_1238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='knack',
            name='thumbnail0',
        ),
        migrations.RemoveField(
            model_name='knack',
            name='thumbnail1',
        ),
        migrations.RemoveField(
            model_name='knack',
            name='thumbnail2',
        ),
        migrations.RemoveField(
            model_name='knack',
            name='thumbnail3',
        ),
        migrations.RemoveField(
            model_name='knack',
            name='thumbnail4',
        ),
    ]
