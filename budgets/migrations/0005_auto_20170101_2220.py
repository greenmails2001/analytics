# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0004_auto_20161231_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='revenues',
            name='end',
            field=models.DateTimeField(db_column='End', default=datetime.datetime(2017, 1, 1, 15, 20, 20, 619834, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='revenues',
            name='progress',
            field=models.DecimalField(max_digits=20, blank=True, null=True, db_column='Progress', decimal_places=3),
        ),
        migrations.AddField(
            model_name='revenues',
            name='revenueratio',
            field=models.DecimalField(max_digits=20, blank=True, null=True, db_column='RevenueRatio', decimal_places=3),
        ),
        migrations.AddField(
            model_name='revenues',
            name='start',
            field=models.DateTimeField(db_column='Start', default=datetime.datetime(2017, 1, 1, 15, 20, 28, 600268, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
