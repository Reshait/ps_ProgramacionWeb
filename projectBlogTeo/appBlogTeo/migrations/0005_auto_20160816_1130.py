# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-16 09:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appBlogTeo', '0004_auto_20160813_2310'),
    ]

    operations = [
        migrations.CreateModel(
            name='Etiqueta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('slug', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='entrada',
            name='etiquetas',
            field=models.ManyToManyField(to='appBlogTeo.Etiqueta'),
        ),
    ]
