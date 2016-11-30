# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0019_auto_20161125_1209'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menufunction',
            options={'ordering': ('orderview', 'name')},
        ),
        migrations.AddField(
            model_name='menufunction',
            name='orderview',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
