# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0023_auto_20161018_1620'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Revenues',
        ),
    ]
