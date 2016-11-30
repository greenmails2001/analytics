# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postage', '0008_auto_20161128_2133'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehicleinout',
            options={'verbose_name_plural': '02. Verhicle In/Out', 'ordering': ('cardtype',), 'verbose_name': '02. Verhicle In/Out'},
        ),
    ]
