# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0036_auto_20161209_0938'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonthlyWeatherByCity',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('month', models.IntegerField()),
                ('boston_temp', models.DecimalField(decimal_places=1, max_digits=5)),
                ('houston_temp', models.DecimalField(decimal_places=1, max_digits=5)),
            ],
        ),
    ]
