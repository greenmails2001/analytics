# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0006_revenues_expenseratio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revenues',
            name='expenseratio',
            field=models.DecimalField(blank=True, decimal_places=3, null=True, max_digits=3, db_column='ExpenseRatio'),
        ),
        migrations.AlterField(
            model_name='revenues',
            name='revenueratio',
            field=models.DecimalField(blank=True, decimal_places=3, null=True, max_digits=3, db_column='RevenueRatio'),
        ),
    ]
