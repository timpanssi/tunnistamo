# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-12 11:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdevice',
            name='auth_counter',
            field=models.PositiveIntegerField(default=0),
        ),
    ]