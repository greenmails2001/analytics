# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0015_auto_20170103_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sites',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
