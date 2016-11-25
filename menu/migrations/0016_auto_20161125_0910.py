# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0015_auto_20161125_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menudetailemployees',
            name='description',
            field=models.TextField(blank=True, max_length=10),
        ),
    ]
