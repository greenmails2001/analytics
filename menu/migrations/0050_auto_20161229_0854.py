# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0049_chart_viewreportby'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chart',
            name='viewreportby',
        ),
        migrations.AddField(
            model_name='chart',
            name='hierarchy',
            field=models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], max_length=50),
        ),
        migrations.AddField(
            model_name='chart',
            name='sqlstring',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chart',
            name='viewreportby2',
            field=models.PositiveIntegerField(blank=True, choices=[(1, 'Chart by Report List'), (2, 'Chart by Data')], default=1),
            preserve_default=False,
        ),
    ]
