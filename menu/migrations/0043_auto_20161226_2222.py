# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0042_auto_20161226_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chart',
            name='charttype',
            field=models.ForeignKey(default=1, related_name='rel_charts_charttypes', to='biapp.ChartType'),
        ),
        migrations.AlterField(
            model_name='chart',
            name='datatype',
            field=models.ForeignKey(default=1, related_name='rel_charts_datatypes', to='biapp.DataType'),
        ),
    ]
