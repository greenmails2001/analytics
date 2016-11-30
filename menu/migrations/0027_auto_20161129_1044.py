# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0026_chart_choices_f'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chart',
            name='choices_f',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='datatype',
            name='name',
            field=models.CharField(max_length=50, db_index=True),
        ),
    ]
