# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0010_auto_20170102_2139'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='profits',
            unique_together=set([]),
        ),
    ]
