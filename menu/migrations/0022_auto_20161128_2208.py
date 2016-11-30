# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0021_auto_20161128_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datatype',
            name='image',
            field=models.ImageField(blank=True, upload_to='image/datatype/%Y/%m/%d'),
        ),
    ]
