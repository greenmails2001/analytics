# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0017_auto_20161018_1457'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='revenues',
            options={'managed': False},
        ),
    ]
