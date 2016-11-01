# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0009_auto_20161018_1354'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profits',
            options={'managed': True},
        ),
        migrations.AddField(
            model_name='profits',
            name='profit_id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False, default=1, db_column='Profit_ID'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='profits',
            unique_together=set([('taskid', 'update', 'sitename')]),
        ),
        migrations.RemoveField(
            model_name='profits',
            name='id',
        ),
    ]
