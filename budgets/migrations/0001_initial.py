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
                ('budgetid', models.PositiveIntegerField(primary_key=True, db_column='BudgetID', serialize=False)),
                ('taskid', models.TextField(db_column='TaskID')),
                ('taskname', models.TextField(db_column='TaskName', null=True, blank=True)),
                ('update', models.DateTimeField(db_column='Update')),
                ('unit', models.TextField(db_column='Unit', null=True, blank=True)),
                ('qty', models.DecimalField(decimal_places=6, db_column='Qty', null=True, max_digits=20, blank=True)),
                ('unitprice', models.DecimalField(decimal_places=6, db_column='UnitPrice', null=True, max_digits=20, blank=True)),
                ('price', models.DecimalField(decimal_places=6, db_column='Price', null=True, max_digits=20, blank=True)),
                ('note', models.TextField(db_column='Note', null=True, blank=True)),
                ('reason', models.TextField(db_column='Reason', null=True, blank=True)),
                ('qtyupt', models.DecimalField(decimal_places=6, db_column='QtyUpt', null=True, max_digits=20, blank=True)),
                ('unitpriceupt', models.DecimalField(decimal_places=6, db_column='UnitPriceUpt', null=True, max_digits=20, blank=True)),
                ('priceupt', models.DecimalField(decimal_places=6, db_column='PriceUpt', null=True, max_digits=20, blank=True)),
                ('noteupt', models.TextField(db_column='NoteUpt', null=True, blank=True)),
                ('reasonupt', models.TextField(db_column='ReasonUpt', null=True, blank=True)),
                ('qtyact', models.DecimalField(decimal_places=6, db_column='QtyAct', null=True, max_digits=20, blank=True)),
                ('priceact', models.DecimalField(decimal_places=6, db_column='PriceAct', null=True, max_digits=20, blank=True)),
                ('noteact', models.TextField(db_column='NoteAct', null=True, blank=True)),
                ('sitename', models.TextField(db_column='SiteName')),
            ],
            options={
                'db_table': 'budgets',
            },
        ),
        migrations.CreateModel(
            name='Profits',
            fields=[
                ('profitid', models.AutoField(primary_key=True, db_column='ProfitID', serialize=False)),
                ('taskid', models.TextField(db_column='TaskID')),
                ('name', models.TextField(db_column='Name', null=True, blank=True)),
                ('update', models.DateTimeField(db_column='Update')),
                ('price', models.FloatField(db_column='Price', null=True, blank=True)),
                ('priceupt', models.FloatField(db_column='PriceUpt', null=True, blank=True)),
                ('priceact', models.FloatField(db_column='PriceAct', null=True, blank=True)),
                ('sitename', models.TextField(db_column='SiteName')),
                ('revenue', models.FloatField(db_column='Revenue', null=True, blank=True)),
                ('revenueupt', models.FloatField(db_column='RevenueUpt', null=True, blank=True)),
                ('revenueact', models.FloatField(db_column='RevenueAct', null=True, blank=True)),
                ('profit', models.FloatField(db_column='Profit', null=True, blank=True)),
                ('profitupt', models.FloatField(db_column='ProfitUpt', null=True, blank=True)),
                ('profitact', models.FloatField(db_column='ProfitAct', null=True, blank=True)),
            ],
            options={
                'db_table': 'profits',
            },
        ),
        migrations.CreateModel(
            name='Revenues',
            fields=[
                ('revenueid', models.AutoField(primary_key=True, db_column='RevenueID', serialize=False)),
                ('sitename', models.TextField(db_column='SiteName')),
                ('revenue', models.DecimalField(decimal_places=6, db_column='Revenue', null=True, max_digits=20, blank=True)),
                ('revenueupt', models.DecimalField(decimal_places=6, db_column='RevenueUpt', null=True, max_digits=20, blank=True)),
                ('revenueact', models.DecimalField(decimal_places=6, db_column='RevenueAct', null=True, max_digits=20, blank=True)),
                ('area', models.DecimalField(decimal_places=6, db_column='Area', null=True, max_digits=20, blank=True)),
                ('unit', models.TextField(db_column='Unit', null=True, blank=True)),
                ('duration', models.DecimalField(decimal_places=6, db_column='Duration', null=True, max_digits=20, blank=True)),
                ('update', models.DateTimeField(db_column='Update')),
                ('note', models.TextField(db_column='Note', null=True, blank=True)),
            ],
            options={
                'db_table': 'revenues',
            },
        ),
        migrations.CreateModel(
            name='Sites',
            fields=[
                ('siteid', models.TextField(primary_key=True, db_column='SiteID', serialize=False)),
                ('sitename', models.TextField(db_column='SiteName', null=True, blank=True)),
                ('manager', models.TextField(db_column='Manager', null=True, blank=True)),
                ('phone', models.TextField(db_column='Phone', null=True, blank=True)),
                ('startdate', models.DateTimeField(db_column='StartDate', null=True, blank=True)),
                ('enddate', models.DateTimeField(db_column='EndDate', null=True, blank=True)),
                ('currentdate', models.DateTimeField(db_column='CurrentDate', null=True, blank=True)),
                ('finished', models.CharField(max_length=1, db_column='Finished', null=True, blank=True)),
                ('area', models.DecimalField(decimal_places=65535, db_column='Area', null=True, max_digits=65535, blank=True)),
                ('imagelink', models.TextField(db_column='ImageLink', null=True, blank=True)),
            ],
            options={
                'db_table': 'sites',
            },
        ),
        migrations.CreateModel(
            name='Tasklist',
            fields=[
                ('taskid', models.TextField(primary_key=True, db_column='TaskID', serialize=False)),
                ('shortname', models.TextField(db_column='ShortName', null=True, blank=True)),
                ('taskname', models.TextField(db_column='TaskName', null=True, blank=True)),
                ('note', models.TextField(db_column='Note', null=True, blank=True)),
            ],
            options={
                'db_table': 'tasklist',
            },
        ),
        migrations.AlterUniqueTogether(
            name='revenues',
            unique_together=set([('update', 'sitename')]),
        ),
        migrations.AlterUniqueTogether(
            name='profits',
            unique_together=set([('taskid', 'update', 'sitename')]),
        ),
        migrations.AlterUniqueTogether(
            name='budgets',
            unique_together=set([('taskid', 'update', 'sitename')]),
        ),
    ]
