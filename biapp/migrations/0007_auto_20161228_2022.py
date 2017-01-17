# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biapp', '0006_auto_20161228_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charttype',
            name='id',
            field=models.CharField(primary_key=True, max_length=20, serialize=False),
        ),
        migrations.AlterField(
            model_name='columnlist',
            name='id',
            field=models.CharField(primary_key=True, max_length=20, serialize=False),
        ),
    ]
