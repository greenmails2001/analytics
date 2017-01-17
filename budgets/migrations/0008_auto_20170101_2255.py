# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0007_auto_20170101_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revenues',
            name='end',
            field=models.DateTimeField(null=True, db_column='End'),
        ),
        migrations.AlterField(
            model_name='revenues',
            name='start',
            field=models.DateTimeField(null=True, db_column='Start'),
        ),
    ]
