# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0011_auto_20170102_2225'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='profits',
            unique_together=set([('taskid', 'update', 'siteid')]),
        ),
    ]
