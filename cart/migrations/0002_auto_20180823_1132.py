# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-23 11:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartmodel',
            name='products',
            field=models.ManyToManyField(to='products.Product'),
        ),
    ]
