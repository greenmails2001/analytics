# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postage', '0002_auto_20161128_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardtype',
            name='orderview',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehiclesupplier',
            name='orderview',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehicletype',
            name='orderview',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
