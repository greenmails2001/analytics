# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0055_auto_20170113_0836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chart',
            name='sqlextra',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='chart',
            name='sqlfilter',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='chart',
            name='sqlstring',
            field=models.TextField(blank=True),
        ),
    ]
