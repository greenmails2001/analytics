# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biapp', '0004_combine'),
        ('menu', '0043_auto_20161226_2222'),
    ]

    operations = [
        migrations.AddField(
            model_name='chart',
            name='axis_x1',
            field=models.ForeignKey(blank=True, related_name='rel_charts_axis_x1', to='biapp.ColumnList', default=1),
        ),
        migrations.AddField(
            model_name='chart',
            name='axis_x2',
            field=models.ForeignKey(blank=True, related_name='rel_charts_axis_x2', to='biapp.ColumnList', default=1),
        ),
        migrations.AddField(
            model_name='chart',
            name='axis_x3',
            field=models.ForeignKey(blank=True, related_name='rel_charts_axis_x3', to='biapp.ColumnList', default=1),
        ),
        migrations.AddField(
            model_name='chart',
            name='axis_x4',
            field=models.ForeignKey(blank=True, related_name='rel_charts_axis_x4', to='biapp.ColumnList', default=1),
        ),
        migrations.AddField(
            model_name='chart',
            name='axis_x5',
            field=models.ForeignKey(blank=True, related_name='rel_charts_axis_x5', to='biapp.ColumnList', default=1),
        ),
        migrations.AddField(
            model_name='chart',
            name='axis_y1',
            field=models.ForeignKey(blank=True, related_name='rel_charts_axis_ý1', to='biapp.ColumnList', default=1),
        ),
        migrations.AddField(
            model_name='chart',
            name='axis_y2',
            field=models.ForeignKey(blank=True, related_name='rel_charts_axis_y2', to='biapp.ColumnList', default=1),
        ),
        migrations.AddField(
            model_name='chart',
            name='axis_y3',
            field=models.ForeignKey(blank=True, related_name='rel_charts_axis_y3', to='biapp.ColumnList', default=1),
        ),
        migrations.AddField(
            model_name='chart',
            name='axis_y4',
            field=models.ForeignKey(blank=True, related_name='rel_charts_axis_y4', to='biapp.ColumnList', default=1),
        ),
        migrations.AddField(
            model_name='chart',
            name='axis_y5',
            field=models.ForeignKey(blank=True, related_name='rel_charts_axis_y5', to='biapp.ColumnList', default=1),
        ),
    ]
