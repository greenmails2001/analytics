# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0041_auto_20161226_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chart',
            name='charttype',
            field=models.ForeignKey(blank=True, related_name='rel_charts_charttypes', to='biapp.ChartType'),
        ),
        migrations.AlterField(
            model_name='chart',
            name='columnlist',
            field=models.ForeignKey(blank=True, related_name='rel_charts_columnlists', to='biapp.ColumnList'),
        ),
        migrations.AlterField(
            model_name='chart',
            name='datatype',
            field=models.ForeignKey(blank=True, related_name='rel_charts_datatypes', to='biapp.DataType'),
        ),
    ]
