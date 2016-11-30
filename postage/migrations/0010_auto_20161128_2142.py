# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postage', '0009_auto_20161128_2135'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='registeredvehicle',
            options={'ordering': ('cardnumber',), 'verbose_name': '--> Registered Vehicle', 'verbose_name_plural': '--> Registered Vehicle'},
        ),
        migrations.AlterModelOptions(
            name='vehicleinout',
            options={'ordering': ('cardtype',), 'verbose_name': '--> Verhicle In/Out', 'verbose_name_plural': '--> Verhicle In/Out'},
        ),
        migrations.AlterModelOptions(
            name='vehiclesupplier',
            options={'ordering': ('id',), 'verbose_name': '03. Vehicle Supplier', 'verbose_name_plural': '03. Vehicle Suppliers'},
        ),
        migrations.AlterModelOptions(
            name='vehicletype',
            options={'ordering': ('id',), 'verbose_name': '02. Vehicle Type', 'verbose_name_plural': '02. Vehicle Types'},
        ),
    ]
