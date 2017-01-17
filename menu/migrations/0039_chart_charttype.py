# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biapp', '0002_auto_20161226_0957'),
        ('menu', '0038_auto_20161226_0927'),
    ]

    operations = [
        migrations.AddField(
            model_name='chart',
            name='charttype',
            field=models.ForeignKey(to='biapp.ChartType', related_name='rel_charts_charttypes', default=1),
            preserve_default=False,
        ),
    ]
