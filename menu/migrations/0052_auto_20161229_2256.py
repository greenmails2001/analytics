# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biapp', '0010_auto_20161228_2110'),
        ('menu', '0051_auto_20161229_0855'),
    ]

    operations = [
        migrations.AddField(
            model_name='chart',
            name='columnlist',
            field=models.ForeignKey(to='biapp.ColumnList', related_name='rel_charts_columnlists', default=1),
        ),
        migrations.AlterField(
            model_name='chart',
            name='hierarchy',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], blank=True, max_length=3),
        ),
    ]
