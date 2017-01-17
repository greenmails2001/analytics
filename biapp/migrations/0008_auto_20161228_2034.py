# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biapp', '0007_auto_20161228_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='charttype',
            name='datatype',
            field=models.ForeignKey(to='biapp.DataType', default='budgets', related_name='rel_charttypes_datatypes'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='columnlist',
            name='datatype',
            field=models.ForeignKey(to='biapp.DataType', default='budgets'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='combine',
            name='datatype',
            field=models.ForeignKey(to='biapp.DataType', default='budgets'),
            preserve_default=False,
        ),
    ]
