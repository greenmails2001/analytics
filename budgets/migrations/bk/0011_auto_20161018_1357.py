# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0010_auto_20161018_1356'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='revenues',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='sites',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='tasklist',
            options={'managed': True},
        ),
    ]
