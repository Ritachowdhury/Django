# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Districts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('education_rate', models.IntegerField()),
                ('population_density', models.IntegerField(null=True, blank=True)),
                ('visited', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Divisions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('population', models.IntegerField()),
                ('area', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='districts',
            name='division',
            field=models.ForeignKey(to='information.Divisions'),
        ),
    ]
