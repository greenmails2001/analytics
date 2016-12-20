# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0035_auto_20161208_2201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='protected_url',
        ),
        migrations.AddField(
            model_name='image',
            name='photo',
            field=models.ImageField(default=1, upload_to='', storage=django.core.files.storage.FileSystemStorage(base_url='/private/', location='D:\\projects\\python\\analytics\\private-media/')),
            preserve_default=False,
        ),
    ]
