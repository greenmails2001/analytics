# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postage', '0010_auto_20161128_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicleinout',
            name='amount',
            field=models.DecimalField(null=True, max_digits=20, blank=True, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='vehicleinout',
            name='charge',
            field=models.DecimalField(null=True, max_digits=20, blank=True, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='vehicleinout',
            name='payin',
            field=models.DecimalField(null=True, max_digits=20, blank=True, decimal_places=2),
        ),
    ]
