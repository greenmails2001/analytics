# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0040_chart_col'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chart',
            old_name='col',
            new_name='columnlist',
        ),
    ]
