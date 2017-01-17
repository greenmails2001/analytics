# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0053_remove_chart_columnlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chart',
            name='datatype',
            field=models.ForeignKey(related_name='rel_charts_datatypes', default='budgets', to='biapp.DataType'),
        ),
    ]
