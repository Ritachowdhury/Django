# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-06 11:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('purpose', models.CharField(max_length=20)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
