# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('postage', '0003_auto_20161128_1845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registeredvehicle',
            name='vehicleuser',
        ),
        migrations.AddField(
            model_name='registeredvehicle',
            name='vehicleuser',
            field=models.ForeignKey(default=1, related_name='rel_vehu_users', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
