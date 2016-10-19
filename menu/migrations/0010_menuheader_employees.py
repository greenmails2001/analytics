# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('menu', '0009_auto_20161010_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuheader',
            name='employees',
            field=models.ManyToManyField(blank=True, related_name='rel_menuheaders_employees', to=settings.AUTH_USER_MODEL),
        ),
    ]
