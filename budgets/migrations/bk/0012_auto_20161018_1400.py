# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0011_auto_20161018_1357'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='budgets',
            options={'managed': True},
        ),
        migrations.RemoveField(
            model_name='sites',
            name='id',
        ),
    ]
