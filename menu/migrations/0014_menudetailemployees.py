# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('menu', '0013_profit_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuDetailEmployees',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('description', models.TextField(blank=True)),
                ('available', models.BooleanField(default=True)),
                ('createddate', models.DateTimeField(auto_now_add=True)),
                ('updateddate', models.DateTimeField(auto_now=True)),
                ('employee', models.ForeignKey(related_name='rel_mdes_users', to=settings.AUTH_USER_MODEL)),
                ('menudetail', models.ForeignKey(related_name='rel_mdes_mds', to='menu.MenuDetail')),
            ],
        ),
    ]
