# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleBrand',
            fields=[
                ('description', models.CharField(max_length=100)),
                ('code', models.SlugField(serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleModel',
            fields=[
                ('description', models.CharField(max_length=100)),
                ('code', models.SlugField(serialize=False, primary_key=True)),
                ('brand', models.ForeignKey(to='testapp.VehicleBrand')),
            ],
        ),
    ]
