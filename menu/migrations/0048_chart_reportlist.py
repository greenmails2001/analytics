# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biapp', '0010_auto_20161228_2110'),
        ('menu', '0047_auto_20161228_2049'),
    ]

    operations = [
        migrations.AddField(
            model_name='chart',
            name='reportlist',
            field=models.ForeignKey(default='rep1', to='biapp.ReportList', related_name='rel_charts_reportlists'),
            preserve_default=False,
        ),
    ]
