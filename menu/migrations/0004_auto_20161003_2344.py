# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_menudetail_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuheader',
            name='image',
            field=models.ImageField(upload_to='image/menuheader/%Y/%m/%d', blank=True),
        ),
        migrations.AlterField(
            model_name='menudetail',
            name='image',
            field=models.ImageField(upload_to='image/menudetail/%Y/%m/%d', blank=True),
        ),
    ]
