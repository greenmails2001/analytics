# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biapp', '0010_auto_20161228_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='columnlist',
            name='datatype',
            field=models.ForeignKey(related_name='rel_columnlists_datatypes', to='biapp.DataType'),
        ),
    ]
