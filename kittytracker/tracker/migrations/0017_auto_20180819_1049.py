# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-08-19 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0016_auto_20180819_0844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carelog',
            name='food_unit_measure',
            field=models.CharField(choices=[('OZ', '(oz) Ounces'), ('LB', '(lb) Pounds'), ('G', '(G) Grams')], default='G', max_length=2),
        ),
        migrations.AlterField(
            model_name='carelog',
            name='medication_dosage_unit',
            field=models.CharField(blank=True, choices=[('ML', '(ml) Milliliters'), ('CC', '(cc) Cubic Centimeters'), ('OZ', '(oz) Ounces'), ('G', '(G) Grams')], help_text='If left blank this will default to the default unit for the medication.', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='carelog',
            name='weight_unit_measure',
            field=models.CharField(choices=[('OZ', '(oz) Ounces'), ('LB', '(lb) Pounds'), ('G', '(G) Grams')], default='G', max_length=2),
        ),
        migrations.AlterField(
            model_name='cat',
            name='weight_unit',
            field=models.CharField(choices=[('OZ', '(oz) Ounces'), ('LB', '(lb) Pounds'), ('G', '(G) Grams')], default='G', max_length=2),
        ),
        migrations.AlterField(
            model_name='medication',
            name='dosage_unit',
            field=models.CharField(blank=True, choices=[('ML', '(ml) Milliliters'), ('CC', '(cc) Cubic Centimeters'), ('OZ', '(oz) Ounces'), ('G', '(G) Grams')], max_length=2, null=True),
        ),
    ]
