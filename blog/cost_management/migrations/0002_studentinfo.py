# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-13 17:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cost_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('fathers_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('phone_number', models.IntegerField()),
            ],
        ),
    ]