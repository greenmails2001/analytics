# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0044_auto_20161226_2248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chart',
            name='charttype',
        ),
        migrations.RemoveField(
            model_name='chart',
            name='columnlist',
        ),
        migrations.RemoveField(
            model_name='chart',
            name='datatype',
        ),
        migrations.AlterField(
            model_name='chart',
            name='axis_x1',
            field=models.CharField(max_length=250, blank=True),
        ),
        migrations.AlterField(
            model_name='chart',
            name='axis_x2',
            field=models.ForeignKey(related_name='rel_charts_axis_x2', to='biapp.ColumnList', blank=True),
        ),
        migrations.AlterField(
            model_name='chart',
            name='axis_x3',
            field=models.ForeignKey(related_name='rel_charts_axis_x3', to='biapp.ColumnList', blank=True),
        ),
        migrations.AlterField(
            model_name='chart',
            name='axis_x4',
            field=models.ForeignKey(related_name='rel_charts_axis_x4', to='biapp.ColumnList', blank=True),
        ),
        migrations.AlterField(
            model_name='chart',
            name='axis_x5',
            field=models.ForeignKey(related_name='rel_charts_axis_x5', to='biapp.ColumnList', blank=True),
        ),
        migrations.AlterField(
            model_name='chart',
            name='axis_y1',
            field=models.ForeignKey(related_name='rel_charts_axis_y1', to='biapp.ColumnList', blank=True),
        ),
        migrations.AlterField(
            model_name='chart',
            name='axis_y2',
            field=models.ForeignKey(related_name='rel_charts_axis_y2', to='biapp.ColumnList', blank=True),
        ),
        migrations.AlterField(
            model_name='chart',
            name='axis_y3',
            field=models.ForeignKey(related_name='rel_charts_axis_y3', to='biapp.ColumnList', blank=True),
        ),
        migrations.AlterField(
            model_name='chart',
            name='axis_y4',
            field=models.ForeignKey(related_name='rel_charts_axis_y4', to='biapp.ColumnList', blank=True),
        ),
        migrations.AlterField(
            model_name='chart',
            name='axis_y5',
            field=models.ForeignKey(related_name='rel_charts_axis_y5', to='biapp.ColumnList', blank=True),
        ),
        migrations.AlterField(
            model_name='chart',
            name='file',
            field=models.FileField(upload_to='charts', blank=True),
        ),
    ]
