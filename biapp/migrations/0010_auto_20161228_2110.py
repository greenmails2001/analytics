# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biapp', '0009_auto_20161228_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportlist',
            name='image',
            field=models.ImageField(upload_to='image/reportlist/%Y/%m/%d', blank=True),
        ),
    ]
