# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataType',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('slug', models.SlugField()),
                ('image', models.ImageField(blank=True, upload_to='image/datatype/%Y/%m/%d')),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AlterIndexTogether(
            name='datatype',
            index_together=set([('id', 'slug')]),
        ),
    ]
