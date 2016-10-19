# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0012_auto_20161018_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='budgets',
            name='budget_id',
            field=models.PositiveIntegerField(default=1, db_column='Budget_ID', primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='budgets',
            unique_together=set([('taskid', 'update', 'sitename')]),
        ),
        migrations.RemoveField(
            model_name='budgets',
            name='id',
        ),
    ]
