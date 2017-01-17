# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0013_auto_20170102_2231'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='revenues',
            unique_together=set([('update', 'siteid')]),
        ),
    ]
