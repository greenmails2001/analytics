# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postage', '0004_auto_20161128_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registeredvehicle',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='registeredvehicle',
            name='idlink',
            field=models.PositiveIntegerField(null=True, db_index=True, blank=True),
        ),
        migrations.AlterField(
            model_name='registeredvehicle',
            name='infor',
            field=models.TextField(max_length=200, null=True, db_index=True, blank=True),
        ),
    ]
