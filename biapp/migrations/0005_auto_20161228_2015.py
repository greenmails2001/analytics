# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biapp', '0004_combine'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='columnlist',
            name='datatype',
        ),
        migrations.RemoveField(
            model_name='combine',
            name='datatype',
        ),
    ]
