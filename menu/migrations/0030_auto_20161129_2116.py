# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0029_auto_20161129_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='charttype',
            name='datatype',
            field=models.ForeignKey(to='menu.DataType', default=1, related_name='rel_charttypes_datatypes'),
            preserve_default=False,
        ),
        migrations.AlterIndexTogether(
            name='datatype',
            index_together=set([('id', 'slug')]),
        ),
    ]
