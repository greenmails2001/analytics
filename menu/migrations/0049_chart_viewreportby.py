# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0048_chart_reportlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='chart',
            name='viewreportby',
            field=models.CharField(choices=[(1, 'Chart by Report List'), (2, 'Chart by Data')], max_length=50, blank=True),
        ),
    ]
