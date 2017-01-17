# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('biapp', '0003_auto_20161226_1047'),
    ]

    operations = [
        migrations.CreateModel(
            name='Combine',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('columnlist', smart_selects.db_fields.ChainedForeignKey(to='biapp.ColumnList', chained_field='datatype', auto_choose=True, chained_model_field='datatype')),
                ('datatype', models.ForeignKey(to='biapp.DataType')),
            ],
        ),
    ]
