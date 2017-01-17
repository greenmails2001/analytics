# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biapp', '0002_auto_20161226_0957'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColumnList',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=50, db_index=True)),
                ('slug', models.SlugField()),
                ('description', models.TextField(blank=True)),
                ('datatype', models.ForeignKey(to='biapp.DataType')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AlterIndexTogether(
            name='columnlist',
            index_together=set([('id', 'slug')]),
        ),
    ]
