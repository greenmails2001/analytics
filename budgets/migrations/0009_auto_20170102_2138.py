# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0008_auto_20170101_2255'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='budgets',
            options={'ordering': ('siteid', 'update', 'taskid'), 'verbose_name': '01. Budgets', 'verbose_name_plural': '01. Budgets'},
        ),
        migrations.AlterModelOptions(
            name='profits',
            options={'ordering': ('siteid', 'update', 'taskid'), 'verbose_name': '03. Profits', 'verbose_name_plural': '03. Profits'},
        ),
        migrations.AlterModelOptions(
            name='revenues',
            options={'ordering': ('siteid', 'update'), 'verbose_name': '02. Revenues', 'verbose_name_plural': '02. Revenues'},
        ),
        migrations.AddField(
            model_name='budgets',
            name='siteid',
            field=models.CharField(max_length=10, default=123, db_column='SiteID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profits',
            name='siteid',
            field=models.CharField(max_length=10, default=123, db_column='SiteID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='revenues',
            name='siteid',
            field=models.CharField(max_length=10, default=123, db_column='SiteID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='revenues',
            name='sitename',
            field=models.CharField(blank=True, null=True, max_length=100, db_column='SiteName'),
        ),
        migrations.AlterField(
            model_name='revenues',
            name='unit',
            field=models.CharField(blank=True, null=True, max_length=10, db_column='Unit'),
        ),
    ]
