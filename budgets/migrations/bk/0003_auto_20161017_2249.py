# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0002_auto_20161017_2243'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='revenues',
            options={},
        ),
        migrations.AlterField(
            model_name='revenues',
            name='id',
            field=models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False),
        ),
        migrations.AlterUniqueTogether(
            name='revenues',
            unique_together=set([('sitename', 'update')]),
        ),
    ]
