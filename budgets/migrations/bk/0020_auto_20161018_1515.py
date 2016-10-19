# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0019_auto_20161018_1514'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='revenues',
            name='id',
        ),
        migrations.AddField(
            model_name='revenues',
            name='rev_id',
            field=models.BigIntegerField(primary_key=True, db_column='Rev_ID', default=1, serialize=False),
            preserve_default=False,
        ),
    ]
