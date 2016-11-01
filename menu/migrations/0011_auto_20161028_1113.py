# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('menu', '0010_menuheader_employees'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=250)),
                ('createddate', models.DateTimeField(auto_now_add=True)),
                ('updateddate', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(upload_to='charts')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ChartType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('image', models.ImageField(upload_to='image/charttype/%Y/%m/%d', blank=True)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AlterIndexTogether(
            name='charttype',
            index_together=set([('id', 'slug')]),
        ),
        migrations.AddField(
            model_name='chart',
            name='charttype',
            field=models.ForeignKey(related_name='rel_charts_charttypes', to='menu.ChartType'),
        ),
        migrations.AddField(
            model_name='chart',
            name='owner',
            field=models.ForeignKey(related_name='chart_related', to=settings.AUTH_USER_MODEL),
        ),
    ]
