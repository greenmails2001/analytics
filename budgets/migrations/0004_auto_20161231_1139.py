# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0003_auto_20161129_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profits',
            name='price',
            field=models.DecimalField(db_column='Price', decimal_places=6, blank=True, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='profits',
            name='priceact',
            field=models.DecimalField(db_column='PriceAct', decimal_places=6, blank=True, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='profits',
            name='priceupt',
            field=models.DecimalField(db_column='PriceUpt', decimal_places=6, blank=True, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='profits',
            name='profit',
            field=models.DecimalField(db_column='Profit', decimal_places=6, blank=True, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='profits',
            name='profitact',
            field=models.DecimalField(db_column='ProfitAct', decimal_places=6, blank=True, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='profits',
            name='profitupt',
            field=models.DecimalField(db_column='ProfitUpt', decimal_places=6, blank=True, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='profits',
            name='revenue',
            field=models.DecimalField(db_column='Revenue', decimal_places=6, blank=True, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='profits',
            name='revenueact',
            field=models.DecimalField(db_column='RevenueAct', decimal_places=6, blank=True, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='profits',
            name='revenueupt',
            field=models.DecimalField(db_column='RevenueUpt', decimal_places=6, blank=True, max_digits=20, null=True),
        ),
    ]
