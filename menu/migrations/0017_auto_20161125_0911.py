# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0016_auto_20161125_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menudetailemployees',
            name='description',
            field=models.CharField(max_length=200, db_index=True),
        ),
    ]
