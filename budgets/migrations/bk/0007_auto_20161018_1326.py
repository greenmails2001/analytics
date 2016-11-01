# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0006_auto_20161017_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revenues',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True),
        ),
    ]
