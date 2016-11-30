# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0028_auto_20161129_1050'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='datatype',
            index_together=set([('name', 'slug')]),
        ),
    ]
