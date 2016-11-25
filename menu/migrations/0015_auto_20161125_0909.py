# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0014_menudetailemployees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menudetailemployees',
            name='description',
            field=models.TextField(max_length=200, blank=True),
        ),
    ]
