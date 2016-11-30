# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postage', '0005_auto_20161128_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicleinout',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='vehicleinout',
            name='idlink',
            field=models.PositiveIntegerField(null=True, blank=True, db_index=True),
        ),
    ]
