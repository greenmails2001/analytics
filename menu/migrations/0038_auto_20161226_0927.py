# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0037_monthlyweatherbycity'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ChartType',
        ),
        migrations.DeleteModel(
            name='DataType',
        ),
        migrations.RemoveField(
            model_name='chart',
            name='charttype',
        ),
        migrations.AlterField(
            model_name='chart',
            name='datatype',
            field=models.ForeignKey(related_name='rel_charts_datatypes', to='biapp.DataType'),
        ),
    ]
