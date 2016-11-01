# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0005_auto_20161017_2321'),
    ]

    operations = [
        migrations.RenameField(
            model_name='revenues',
            old_name='revenue_id',
            new_name='id',
        ),
    ]
