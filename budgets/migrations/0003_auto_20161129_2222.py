# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0002_sites_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='budgets',
            options={'ordering': ('sitename', 'update', 'taskid'), 'verbose_name_plural': '01. Budgets', 'verbose_name': '01. Budgets'},
        ),
        migrations.AlterModelOptions(
            name='profits',
            options={'ordering': ('sitename', 'update', 'taskid'), 'verbose_name_plural': '03. Profits', 'verbose_name': '03. Profits'},
        ),
        migrations.AlterModelOptions(
            name='revenues',
            options={'ordering': ('sitename', 'update'), 'verbose_name_plural': '02. Revenues', 'verbose_name': '02. Revenues'},
        ),
        migrations.AlterModelOptions(
            name='sites',
            options={'ordering': ('sitename',), 'verbose_name_plural': '04. Sites', 'verbose_name': '04. Sites'},
        ),
        migrations.AlterModelOptions(
            name='tasklist',
            options={'ordering': ('taskid',), 'verbose_name_plural': '05. Task Lists', 'verbose_name': '05. Task Lists'},
        ),
    ]
