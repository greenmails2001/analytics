# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0005_auto_20170101_2220'),
    ]

    operations = [
        migrations.AddField(
            model_name='revenues',
            name='expenseratio',
            field=models.DecimalField(blank=True, null=True, decimal_places=3, max_digits=20, db_column='ExpenseRatio'),
        ),
    ]
