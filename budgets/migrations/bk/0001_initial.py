# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Budgets',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('taskid', models.TextField(db_column='TaskID')),
                ('taskname', models.TextField(blank=True, null=True, db_column='TaskName')),
                ('update', models.DateTimeField(db_column='Update')),
                ('unit', models.TextField(blank=True, null=True, db_column='Unit')),
                ('qty', models.DecimalField(blank=True, null=True, max_digits=65535, decimal_places=65535, db_column='Qty')),
                ('unitprice', models.DecimalField(blank=True, null=True, max_digits=65535, decimal_places=65535, db_column='UnitPrice')),
                ('price', models.DecimalField(blank=True, null=True, max_digits=65535, decimal_places=65535, db_column='Price')),
                ('note', models.TextField(blank=True, null=True, db_column='Note')),
                ('reason', models.TextField(blank=True, null=True, db_column='Reason')),
                ('qtyupt', models.DecimalField(blank=True, null=True, max_digits=65535, decimal_places=65535, db_column='QtyUpt')),
                ('unitpriceupt', models.DecimalField(blank=True, null=True, max_digits=65535, decimal_places=65535, db_column='UnitPriceUpt')),
                ('priceupt', models.DecimalField(blank=True, null=True, max_digits=65535, decimal_places=65535, db_column='PriceUpt')),
                ('noteupt', models.TextField(blank=True, null=True, db_column='NoteUpt')),
                ('reasonupt', models.TextField(blank=True, null=True, db_column='ReasonUpt')),
                ('qtyact', models.DecimalField(blank=True, null=True, max_digits=65535, decimal_places=65535, db_column='QtyAct')),
                ('priceact', models.DecimalField(blank=True, null=True, max_digits=65535, decimal_places=65535, db_column='PriceAct')),
                ('noteact', models.TextField(blank=True, null=True, db_column='NoteAct')),
                ('sitename', models.TextField(db_column='SiteName')),
            ],
            options={
                'db_table': 'budgets',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Profits',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('taskid', models.TextField(db_column='TaskID')),
                ('name', models.TextField(blank=True, null=True, db_column='Name')),
                ('update', models.DateTimeField(db_column='Update')),
                ('price', models.FloatField(blank=True, null=True, db_column='Price')),
                ('priceupt', models.FloatField(blank=True, null=True, db_column='PriceUpt')),
                ('priceact', models.FloatField(blank=True, null=True, db_column='PriceAct')),
                ('sitename', models.TextField(db_column='SiteName')),
                ('revenue', models.FloatField(blank=True, null=True, db_column='Revenue')),
                ('revenueupt', models.FloatField(blank=True, null=True, db_column='RevenueUpt')),
                ('revenueact', models.FloatField(blank=True, null=True, db_column='RevenueAct')),
                ('profit', models.FloatField(blank=True, null=True, db_column='Profit')),
                ('profitupt', models.FloatField(blank=True, null=True, db_column='ProfitUpt')),
                ('profitact', models.FloatField(blank=True, null=True, db_column='ProfitAct')),
            ],
            options={
                'db_table': 'profits',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Revenues',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('sitename', models.TextField(db_column='SiteName')),
                ('revenue', models.DecimalField(blank=True, null=True, max_digits=65535, decimal_places=65535, db_column='Revenue')),
                ('revenueupt', models.DecimalField(blank=True, null=True, max_digits=65535, decimal_places=65535, db_column='RevenueUpt')),
                ('revenueact', models.DecimalField(blank=True, null=True, max_digits=65535, decimal_places=65535, db_column='RevenueAct')),
                ('area', models.DecimalField(blank=True, null=True, max_digits=65535, decimal_places=65535, db_column='Area')),
                ('unit', models.TextField(blank=True, null=True, db_column='Unit')),
                ('duration', models.DecimalField(blank=True, null=True, max_digits=65535, decimal_places=65535, db_column='Duration')),
                ('update', models.DateTimeField(db_column='Update')),
            ],
            options={
                'db_table': 'revenues',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sites',
            fields=[
                ('id', models.AutoField(primary_key=True)),
                ('siteid', models.TextField(primary_key=True, serialize=False, db_column='SiteID')),
                ('sitename', models.TextField(blank=True, null=True, db_column='SiteName')),
                ('manager', models.TextField(blank=True, null=True, db_column='Manager')),
                ('phone', models.TextField(blank=True, null=True, db_column='Phone')),
                ('startdate', models.DateTimeField(blank=True, null=True, db_column='StartDate')),
                ('enddate', models.DateTimeField(blank=True, null=True, db_column='EndDate')),
                ('currentdate', models.DateTimeField(blank=True, null=True, db_column='CurrentDate')),
                ('finished', models.CharField(blank=True, null=True, max_length=1, db_column='Finished')),
                ('area', models.DecimalField(blank=True, null=True, max_digits=65535, decimal_places=65535, db_column='Area')),
                ('imagelink', models.TextField(blank=True, null=True, db_column='ImageLink')),
            ],
            options={
                'db_table': 'sites',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tasklist',
            fields=[
                ('taskid', models.TextField(primary_key=True, serialize=False, db_column='TaskID')),
                ('shortname', models.TextField(blank=True, null=True, db_column='ShortName')),
                ('taskname', models.TextField(blank=True, null=True, db_column='TaskName')),
                ('note', models.TextField(blank=True, null=True, db_column='Note')),
            ],
            options={
                'db_table': 'tasklist',
                'managed': False,
            },
        ),
    ]
