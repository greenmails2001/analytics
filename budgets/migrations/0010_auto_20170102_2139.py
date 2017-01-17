# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0009_auto_20170102_2138'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='budgets',
            unique_together=set([('taskid', 'update', 'siteid')]),
        ),
    ]
