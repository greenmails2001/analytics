# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0025_remove_chart_siteid'),
    ]

    operations = [
        migrations.AddField(
            model_name='chart',
            name='choices_f',
            field=models.CharField(max_length=8, blank=True),
        ),
    ]
