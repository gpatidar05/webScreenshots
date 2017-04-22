# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-20 20:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('link', models.CharField(max_length=255)),
                ('screenshot', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
