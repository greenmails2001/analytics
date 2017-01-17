# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0050_auto_20161229_0854'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chart',
            name='viewreportby2',
        ),
        migrations.AddField(
            model_name='chart',
            name='viewreportby',
            field=models.PositiveIntegerField(default=1, choices=[(1, 'Chart by Report List'), (2, 'Chart by Data')], blank=True),
        ),
    ]
