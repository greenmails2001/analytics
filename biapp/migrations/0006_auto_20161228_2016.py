# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biapp', '0005_auto_20161228_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datatype',
            name='id',
            field=models.CharField(serialize=False, primary_key=True, max_length=20),
        ),
    ]
