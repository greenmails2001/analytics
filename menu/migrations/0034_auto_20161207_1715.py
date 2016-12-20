# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0033_auto_20161207_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chart',
            name='size',
            field=models.CharField(choices=[('2', 'Size 2/12'), ('3', 'Size 3/12'), ('4', 'Size 4/12'), ('5', 'Size 5/12'), ('6', 'Size 6/12'), ('7', 'Size 7/12'), ('8', 'Size 8/12'), ('9', 'Size 9/12'), ('10', 'Size 10/12'), ('11', 'Size 11/12'), ('12', 'Size 12/12')], default=6, max_length=2, blank=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='size',
            field=models.CharField(choices=[('2', 'Size 2/12'), ('3', 'Size 3/12'), ('4', 'Size 4/12'), ('5', 'Size 5/12'), ('6', 'Size 6/12'), ('7', 'Size 7/12'), ('8', 'Size 8/12'), ('9', 'Size 9/12'), ('10', 'Size 10/12'), ('11', 'Size 11/12'), ('12', 'Size 12/12')], default=6, max_length=2, blank=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='size',
            field=models.CharField(choices=[('2', 'Size 2/12'), ('3', 'Size 3/12'), ('4', 'Size 4/12'), ('5', 'Size 5/12'), ('6', 'Size 6/12'), ('7', 'Size 7/12'), ('8', 'Size 8/12'), ('9', 'Size 9/12'), ('10', 'Size 10/12'), ('11', 'Size 11/12'), ('12', 'Size 12/12')], default=6, max_length=2, blank=True),
        ),
        migrations.AlterField(
            model_name='profit_table',
            name='size',
            field=models.CharField(choices=[('2', 'Size 2/12'), ('3', 'Size 3/12'), ('4', 'Size 4/12'), ('5', 'Size 5/12'), ('6', 'Size 6/12'), ('7', 'Size 7/12'), ('8', 'Size 8/12'), ('9', 'Size 9/12'), ('10', 'Size 10/12'), ('11', 'Size 11/12'), ('12', 'Size 12/12')], default=6, max_length=2, blank=True),
        ),
        migrations.AlterField(
            model_name='text',
            name='size',
            field=models.CharField(choices=[('2', 'Size 2/12'), ('3', 'Size 3/12'), ('4', 'Size 4/12'), ('5', 'Size 5/12'), ('6', 'Size 6/12'), ('7', 'Size 7/12'), ('8', 'Size 8/12'), ('9', 'Size 9/12'), ('10', 'Size 10/12'), ('11', 'Size 11/12'), ('12', 'Size 12/12')], default=6, max_length=2, blank=True),
        ),
        migrations.AlterField(
            model_name='url',
            name='size',
            field=models.CharField(choices=[('2', 'Size 2/12'), ('3', 'Size 3/12'), ('4', 'Size 4/12'), ('5', 'Size 5/12'), ('6', 'Size 6/12'), ('7', 'Size 7/12'), ('8', 'Size 8/12'), ('9', 'Size 9/12'), ('10', 'Size 10/12'), ('11', 'Size 11/12'), ('12', 'Size 12/12')], default=6, max_length=2, blank=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='size',
            field=models.CharField(choices=[('2', 'Size 2/12'), ('3', 'Size 3/12'), ('4', 'Size 4/12'), ('5', 'Size 5/12'), ('6', 'Size 6/12'), ('7', 'Size 7/12'), ('8', 'Size 8/12'), ('9', 'Size 9/12'), ('10', 'Size 10/12'), ('11', 'Size 11/12'), ('12', 'Size 12/12')], default=6, max_length=2, blank=True),
        ),
    ]
