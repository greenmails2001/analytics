# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0045_auto_20161228_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chart',
            name='axis_x1',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='chart',
            name='axis_x2',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='chart',
            name='axis_x3',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='chart',
            name='axis_x4',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='chart',
            name='axis_x5',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='chart',
            name='axis_y1',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='chart',
            name='axis_y2',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='chart',
            name='axis_y3',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='chart',
            name='axis_y4',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='chart',
            name='axis_y5',
            field=models.CharField(max_length=20, blank=True),
        ),
    ]
