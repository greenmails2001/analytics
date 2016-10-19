# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200)),
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
            name='MenuHeader',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('description', models.TextField(blank=True)),
                ('orderview', models.PositiveIntegerField()),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'menu header',
                'verbose_name_plural': 'menu headers',
            },
        ),
        migrations.RenameModel(
            old_name='Menu_Function',
            new_name='MenuFunction',
        ),
        migrations.AlterIndexTogether(
            name='menu_detail',
            index_together=set([]),
        ),
        migrations.RemoveField(
            model_name='menu_detail',
            name='menu_header',
        ),
        migrations.RemoveField(
            model_name='menu_header',
            name='menu_function',
        ),
        migrations.RemoveField(
            model_name='menu_header',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Menu_Detail',
        ),
        migrations.DeleteModel(
            name='Menu_Header',
        ),
        migrations.AddField(
            model_name='menuheader',
            name='menufunction',
            field=models.ForeignKey(to='menu.MenuFunction', related_name='rel_menu_headers_functions'),
        ),
        migrations.AddField(
            model_name='menuheader',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='rel_menu_headers_users'),
        ),
        migrations.AddField(
            model_name='menudetail',
            name='menuheader',
            field=models.ForeignKey(to='menu.MenuHeader', related_name='rel_menu_details'),
        ),
        migrations.AlterIndexTogether(
            name='menudetail',
            index_together=set([('id', 'slug')]),
        ),
    ]
