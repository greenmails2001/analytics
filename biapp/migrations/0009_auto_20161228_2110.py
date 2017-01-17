# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biapp', '0008_auto_20161228_2034'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportList',
            fields=[
                ('id', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200, db_index=True)),
                ('slug', models.SlugField(max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='image/charttype/%Y/%m/%d')),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AlterIndexTogether(
            name='reportlist',
            index_together=set([('id', 'slug')]),
        ),
    ]
