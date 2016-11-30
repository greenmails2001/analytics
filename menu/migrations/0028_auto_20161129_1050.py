# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0027_auto_20161129_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datatype',
            name='slug',
            field=models.SlugField(),
        ),
    ]
