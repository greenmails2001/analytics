# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0014_auto_20170102_2232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='budgets',
            name='sitename',
        ),
        migrations.RemoveField(
            model_name='profits',
            name='sitename',
        ),
        migrations.RemoveField(
            model_name='revenues',
            name='sitename',
        ),
        migrations.AlterField(
            model_name='sites',
            name='sitename',
            field=models.TextField(db_column='SiteName', null=True, max_length=100, blank=True),
        ),
    ]
