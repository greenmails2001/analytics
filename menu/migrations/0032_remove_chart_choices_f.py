# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0031_remove_charttype_datatype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chart',
            name='choices_f',
        ),
    ]
