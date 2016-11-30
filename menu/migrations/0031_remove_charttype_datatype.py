# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0030_auto_20161129_2116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='charttype',
            name='datatype',
        ),
    ]
