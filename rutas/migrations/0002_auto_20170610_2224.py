# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-10 20:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rutas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ruta',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]