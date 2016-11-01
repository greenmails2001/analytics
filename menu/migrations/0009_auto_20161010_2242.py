# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0008_auto_20161010_2034'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemcontent',
            old_name='itemid',
            new_name='objid',
        ),
    ]
