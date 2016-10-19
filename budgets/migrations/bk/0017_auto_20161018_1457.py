# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0016_auto_20161018_1449'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='revenues',
            unique_together=set([]),
        ),
    ]
