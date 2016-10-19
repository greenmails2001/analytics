# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0021_auto_20161018_1520'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='revenues',
            options={},
        ),
        migrations.RemoveField(
            model_name='revenues',
            name='rev_id',
        ),
        migrations.AddField(
            model_name='revenues',
            name='id',
            field=models.AutoField(auto_created=True, verbose_name='ID', default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
