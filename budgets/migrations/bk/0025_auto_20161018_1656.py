# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0024_delete_revenues'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Budgets',
        ),
        migrations.DeleteModel(
            name='Profits',
        ),
    ]
