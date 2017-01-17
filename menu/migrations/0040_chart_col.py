# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('biapp', '0003_auto_20161226_1047'),
        ('menu', '0039_chart_charttype'),
    ]

    operations = [
        migrations.AddField(
            model_name='chart',
            name='col',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='datatype', auto_choose=True, to='biapp.ColumnList', chained_model_field='datatype', default=14),
            preserve_default=False,
        ),
    ]
