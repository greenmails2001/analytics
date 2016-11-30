# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postage', '0007_auto_20161128_2113'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cardtype',
            options={'verbose_name_plural': '01. Cart Types', 'ordering': ('id',), 'verbose_name': '01. Cart Type'},
        ),
    ]
