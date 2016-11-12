# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0001_initial'),
        ('menu', '0011_auto_20161028_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='chart',
            name='siteid',
            field=models.ForeignKey(to='budgets.Sites', default=118, related_name='rel_charts_sites'),
            preserve_default=False,
        ),
    ]
