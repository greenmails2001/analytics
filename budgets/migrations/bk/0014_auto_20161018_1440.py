# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0013_auto_20161018_1417'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='revenues',
            name='revenue_id',
        ),
        migrations.AddField(
            model_name='revenues',
            name='id',
            field=models.PositiveIntegerField(db_column='ID', serialize=False, primary_key=True, default=1),
            preserve_default=False,
        ),
    ]
