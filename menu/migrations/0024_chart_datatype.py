# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0023_auto_20161128_2249'),
    ]

    operations = [
        migrations.AddField(
            model_name='chart',
            name='datatype',
            field=models.ForeignKey(default=1, to='menu.DataType', related_name='rel_charts_datatypes'),
            preserve_default=False,
        ),
    ]
