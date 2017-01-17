# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0054_auto_20161230_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='chart',
            name='sqlextra',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chart',
            name='sqlfilter',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
