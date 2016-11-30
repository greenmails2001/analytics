# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0022_auto_20161128_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='chart',
            name='content',
            field=models.TextField(default=''),
            preserve_default=False,
        ),

    ]
