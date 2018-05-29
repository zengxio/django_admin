# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-05-29 03:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]