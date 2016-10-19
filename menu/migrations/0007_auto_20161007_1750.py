# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_auto_20161005_1327'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='created',
            new_name='createddate',
        ),
        migrations.RenameField(
            model_name='file',
            old_name='updated',
            new_name='updateddate',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='created',
            new_name='createddate',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='updated',
            new_name='updateddate',
        ),
        migrations.RenameField(
            model_name='menudetail',
            old_name='created',
            new_name='createddate',
        ),
        migrations.RenameField(
            model_name='menudetail',
            old_name='updated',
            new_name='updateddate',
        ),
        migrations.RenameField(
            model_name='menuheader',
            old_name='created',
            new_name='createddate',
        ),
        migrations.RenameField(
            model_name='menuheader',
            old_name='updated',
            new_name='updateddate',
        ),
        migrations.RenameField(
            model_name='text',
            old_name='created',
            new_name='createddate',
        ),
        migrations.RenameField(
            model_name='text',
            old_name='updated',
            new_name='updateddate',
        ),
        migrations.RenameField(
            model_name='video',
            old_name='created',
            new_name='createddate',
        ),
        migrations.RenameField(
            model_name='video',
            old_name='updated',
            new_name='updateddate',
        ),
    ]
