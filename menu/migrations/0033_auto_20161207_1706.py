# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0032_remove_chart_choices_f'),
    ]

    operations = [
        migrations.AddField(
            model_name='chart',
            name='haveLink',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='chart',
            name='haveTitle',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='chart',
            name='size',
            field=models.PositiveIntegerField(default=6, blank=True, choices=[(2, 'Size 2/12'), (3, 'Size 3/12'), (4, 'Size 4/12'), (5, 'Size 5/12'), (6, 'Size 6/12'), (7, 'Size 7/12'), (8, 'Size 8/12'), (9, 'Size 9/12'), (10, 'Size 10/12'), (11, 'Size 11/12'), (12, 'Size 12/12')]),
        ),
        migrations.AddField(
            model_name='file',
            name='haveLink',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='file',
            name='haveTitle',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='file',
            name='size',
            field=models.PositiveIntegerField(default=6, blank=True, choices=[(2, 'Size 2/12'), (3, 'Size 3/12'), (4, 'Size 4/12'), (5, 'Size 5/12'), (6, 'Size 6/12'), (7, 'Size 7/12'), (8, 'Size 8/12'), (9, 'Size 9/12'), (10, 'Size 10/12'), (11, 'Size 11/12'), (12, 'Size 12/12')]),
        ),
        migrations.AddField(
            model_name='image',
            name='haveLink',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='image',
            name='haveTitle',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='image',
            name='size',
            field=models.PositiveIntegerField(default=6, blank=True, choices=[(2, 'Size 2/12'), (3, 'Size 3/12'), (4, 'Size 4/12'), (5, 'Size 5/12'), (6, 'Size 6/12'), (7, 'Size 7/12'), (8, 'Size 8/12'), (9, 'Size 9/12'), (10, 'Size 10/12'), (11, 'Size 11/12'), (12, 'Size 12/12')]),
        ),
        migrations.AddField(
            model_name='profit_table',
            name='haveLink',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profit_table',
            name='haveTitle',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='profit_table',
            name='size',
            field=models.PositiveIntegerField(default=6, blank=True, choices=[(2, 'Size 2/12'), (3, 'Size 3/12'), (4, 'Size 4/12'), (5, 'Size 5/12'), (6, 'Size 6/12'), (7, 'Size 7/12'), (8, 'Size 8/12'), (9, 'Size 9/12'), (10, 'Size 10/12'), (11, 'Size 11/12'), (12, 'Size 12/12')]),
        ),
        migrations.AddField(
            model_name='text',
            name='haveLink',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='text',
            name='haveTitle',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='text',
            name='size',
            field=models.PositiveIntegerField(default=6, blank=True, choices=[(2, 'Size 2/12'), (3, 'Size 3/12'), (4, 'Size 4/12'), (5, 'Size 5/12'), (6, 'Size 6/12'), (7, 'Size 7/12'), (8, 'Size 8/12'), (9, 'Size 9/12'), (10, 'Size 10/12'), (11, 'Size 11/12'), (12, 'Size 12/12')]),
        ),
        migrations.AddField(
            model_name='url',
            name='haveLink',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='url',
            name='haveTitle',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='url',
            name='size',
            field=models.PositiveIntegerField(default=6, blank=True, choices=[(2, 'Size 2/12'), (3, 'Size 3/12'), (4, 'Size 4/12'), (5, 'Size 5/12'), (6, 'Size 6/12'), (7, 'Size 7/12'), (8, 'Size 8/12'), (9, 'Size 9/12'), (10, 'Size 10/12'), (11, 'Size 11/12'), (12, 'Size 12/12')]),
        ),
        migrations.AddField(
            model_name='video',
            name='haveLink',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='video',
            name='haveTitle',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='video',
            name='size',
            field=models.PositiveIntegerField(default=6, blank=True, choices=[(2, 'Size 2/12'), (3, 'Size 3/12'), (4, 'Size 4/12'), (5, 'Size 5/12'), (6, 'Size 6/12'), (7, 'Size 7/12'), (8, 'Size 8/12'), (9, 'Size 9/12'), (10, 'Size 10/12'), (11, 'Size 11/12'), (12, 'Size 12/12')]),
        ),
    ]
