# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20161003_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='menudetail',
            name='image',
            field=models.ImageField(blank=True, upload_to='image/%Y/%m/%d'),
        ),
    ]
