# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('menu', '0032_remove_chart_choices_f'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemContentGroups',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('description', models.TextField(max_length=200, blank=True)),
                ('available', models.BooleanField(default=True, db_index=True)),
                ('createddate', models.DateTimeField(auto_now_add=True)),
                ('updateddate', models.DateTimeField(auto_now=True)),
                ('group', models.ForeignKey(to='auth.Group', related_name='rel_ictgs_groups')),
                ('itemcontent', models.ForeignKey(to='menu.ItemContent', related_name='rel_ictgs_icts')),
            ],
        ),
        migrations.CreateModel(
            name='MenuDetailGroups',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('description', models.TextField(max_length=200, blank=True)),
                ('available', models.BooleanField(default=True)),
                ('createddate', models.DateTimeField(auto_now_add=True)),
                ('updateddate', models.DateTimeField(auto_now=True)),
                ('group', models.ForeignKey(to='auth.Group', related_name='rel_mdgs_groups')),
                ('menudetail', models.ForeignKey(to='menu.MenuDetail', related_name='rel_mdgs_mds')),
            ],
        ),
        migrations.CreateModel(
            name='MenuFunctionGroups',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('description', models.TextField(max_length=200, blank=True)),
                ('available', models.BooleanField(default=True)),
                ('createddate', models.DateTimeField(auto_now_add=True)),
                ('updateddate', models.DateTimeField(auto_now=True)),
                ('group', models.ForeignKey(to='auth.Group', related_name='rel_mfgs_groups')),
                ('menufunction', models.ForeignKey(to='menu.MenuFunction', related_name='rel_mfgs_mfs')),
            ],
        ),
        migrations.CreateModel(
            name='MenuHeaderGroups',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('description', models.TextField(max_length=200, blank=True)),
                ('available', models.BooleanField(default=True)),
                ('createddate', models.DateTimeField(auto_now_add=True)),
                ('updateddate', models.DateTimeField(auto_now=True)),
                ('group', models.ForeignKey(to='auth.Group', related_name='rel_mhgs_groups')),
                ('menuheader', models.ForeignKey(to='menu.MenuHeader', related_name='rel_mhgs_mhs')),
            ],
        ),
    ]
