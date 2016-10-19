# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sites',
            fields=[
                ('siteid', models.TextField(primary_key=True, db_column='SiteID', serialize=False)),
                ('sitename', models.TextField(null=True, db_column='SiteName', blank=True)),
                ('manager', models.TextField(null=True, db_column='Manager', blank=True)),
                ('phone', models.TextField(null=True, db_column='Phone', blank=True)),
                ('startdate', models.DateTimeField(null=True, db_column='StartDate', blank=True)),
                ('enddate', models.DateTimeField(null=True, db_column='EndDate', blank=True)),
                ('currentdate', models.DateTimeField(null=True, db_column='CurrentDate', blank=True)),
                ('finished', models.CharField(null=True, db_column='Finished', blank=True, max_length=1)),
                ('area', models.DecimalField(max_digits=65535, decimal_places=65535, null=True, db_column='Area', blank=True)),
                ('imagelink', models.TextField(null=True, db_column='ImageLink', blank=True)),
            ],
            options={
                'db_table': 'sites',
            },
        ),
        migrations.CreateModel(
            name='Tasklist',
            fields=[
                ('taskid', models.TextField(primary_key=True, db_column='TaskID', serialize=False)),
                ('shortname', models.TextField(null=True, db_column='ShortName', blank=True)),
                ('taskname', models.TextField(null=True, db_column='TaskName', blank=True)),
                ('note', models.TextField(null=True, db_column='Note', blank=True)),
            ],
            options={
                'db_table': 'tasklist',
            },
        ),
        migrations.CreateModel(
            name='TestProfits',
            fields=[
                ('profitid', models.PositiveIntegerField(primary_key=True, db_column='ProfitID', serialize=False)),
                ('taskid', models.TextField(db_column='TaskID')),
                ('name', models.TextField(null=True, db_column='Name', blank=True)),
                ('update', models.DateTimeField(db_column='Update')),
                ('price', models.FloatField(null=True, db_column='Price', blank=True)),
                ('priceupt', models.FloatField(null=True, db_column='PriceUpt', blank=True)),
                ('priceact', models.FloatField(null=True, db_column='PriceAct', blank=True)),
                ('sitename', models.TextField(db_column='SiteName')),
                ('revenue', models.FloatField(null=True, db_column='Revenue', blank=True)),
                ('revenueupt', models.FloatField(null=True, db_column='RevenueUpt', blank=True)),
                ('revenueact', models.FloatField(null=True, db_column='RevenueAct', blank=True)),
                ('profit', models.FloatField(null=True, db_column='Profit', blank=True)),
                ('profitupt', models.FloatField(null=True, db_column='ProfitUpt', blank=True)),
                ('profitact', models.FloatField(null=True, db_column='ProfitAct', blank=True)),
            ],
            options={
                'db_table': 'testprofits',
            },
        ),
        migrations.AlterUniqueTogether(
            name='testprofits',
            unique_together=set([('taskid', 'update', 'sitename')]),
        ),
    ]
