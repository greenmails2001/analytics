# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0014_auto_20161018_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revenues',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False, db_column='id'),
        ),
    ]
