# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0004_auto_20161017_2320'),
    ]

    operations = [
        migrations.RenameField(
            model_name='revenues',
            old_name='id',
            new_name='revenue_id',
        ),
    ]
