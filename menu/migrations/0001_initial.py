# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu_Detail',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200, db_index=True)),
                ('slug', models.SlugField(max_length=200)),
                ('image', models.ImageField(upload_to='menu_details/%Y/%m/%d', blank=True)),
                ('description', models.TextField(blank=True)),
                ('orderview', models.PositiveIntegerField()),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Menu_Function',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Menu_Header',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200, db_index=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('description', models.TextField(blank=True)),
                ('orderview', models.PositiveIntegerField()),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('menu_function', models.ForeignKey(related_name='rel_menu_headers_functions', to='menu.Menu_Function')),
                ('owner', models.ForeignKey(related_name='rel_menu_headers_users', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name_plural': 'menu headers',
                'verbose_name': 'menu header',
            },
        ),
        migrations.AddField(
            model_name='menu_detail',
            name='menu_header',
            field=models.ForeignKey(related_name='rel_menu_details', to='menu.Menu_Header'),
        ),
        migrations.AlterIndexTogether(
            name='menu_detail',
            index_together=set([('id', 'slug')]),
        ),
    ]
