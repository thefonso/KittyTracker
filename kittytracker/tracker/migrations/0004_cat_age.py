# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-06-24 14:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_auto_20180624_0027'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='age',
            field=models.CharField(choices=[('A', 'Adult'), ('K', 'Kitten')], default=None, max_length=1),
        ),
    ]
