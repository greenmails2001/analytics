# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='revenues',
            options={'managed': True},
        ),
    ]
