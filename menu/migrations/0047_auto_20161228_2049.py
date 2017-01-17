# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biapp', '0008_auto_20161228_2034'),
        ('menu', '0046_auto_20161228_2011'),
    ]

    operations = [
        migrations.AddField(
            model_name='chart',
            name='charttype',
            field=models.ForeignKey(related_name='rel_charts_charttypes', to='biapp.ChartType', default='line'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chart',
            name='datatype',
            field=models.ForeignKey(related_name='rel_charts_datatypes', to='biapp.DataType', default='budgets'),
            preserve_default=False,
        ),
    ]
