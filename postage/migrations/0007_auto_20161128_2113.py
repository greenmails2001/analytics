# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postage', '0006_auto_20161128_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardtype',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cardtype',
            name='orderview',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vehiclesupplier',
            name='idlink',
            field=models.PositiveIntegerField(blank=True, null=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='vehiclesupplier',
            name='infor',
            field=models.TextField(blank=True, db_index=True, null=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='vehiclesupplier',
            name='orderview',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vehicletype',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vehicletype',
            name='orderview',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
