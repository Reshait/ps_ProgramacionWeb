# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-13 21:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appBlogTeo', '0003_auto_20160813_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='autor',
            field=models.CharField(default='Anonimo', max_length=100),
        ),
    ]
