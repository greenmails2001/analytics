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
            name='CardType',
            fields=[
                ('id', models.CharField(serialize=False, max_length=50, primary_key=True)),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField()),
                ('image', models.ImageField(blank=True, upload_to='image/cardtype/%Y/%m/%d')),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='VehicleCard',
            fields=[
                ('id', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('cardnumber', models.CharField(db_index=True, max_length=50)),
                ('vehicleowner', models.CharField(db_index=True, max_length=50)),
                ('vehiclenumber', models.CharField(db_index=True, max_length=50)),
                ('registerdate', models.DateTimeField()),
                ('enddate', models.DateTimeField()),
                ('startdate', models.DateTimeField()),
                ('infor', models.TextField(db_index=True, max_length=200)),
                ('status', models.CharField(db_index=True, max_length=5)),
                ('createddate', models.DateTimeField(auto_now_add=True)),
                ('updateddate', models.DateTimeField(auto_now=True)),
                ('idlink', models.PositiveIntegerField(db_index=True)),
                ('cardtype', models.ForeignKey(related_name='rel_vehc_cardtypes', to='postage.CardType')),
            ],
            options={
                'ordering': ('cardnumber',),
            },
        ),
        migrations.CreateModel(
            name='VehicleInOut',
            fields=[
                ('id', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('vehiclenumber', models.CharField(db_index=True, max_length=10)),
                ('checkin', models.DateTimeField()),
                ('checkout', models.DateTimeField()),
                ('stationnamein', models.CharField(db_index=True, max_length=50)),
                ('stationnameout', models.CharField(db_index=True, max_length=50)),
                ('status', models.CharField(db_index=True, max_length=5)),
                ('createddate', models.DateTimeField(auto_now_add=True)),
                ('updateddate', models.DateTimeField(auto_now=True)),
                ('idlink', models.PositiveIntegerField(db_index=True)),
                ('cardtype', models.ForeignKey(related_name='rel_vehio_cardtypes', to='postage.CardType')),
            ],
            options={
                'ordering': ('cardtype',),
            },
        ),
        migrations.CreateModel(
            name='VehicleSupplier',
            fields=[
                ('id', models.CharField(serialize=False, max_length=50, primary_key=True)),
                ('slug', models.SlugField()),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slotnumber', models.PositiveIntegerField(db_index=True)),
                ('registerdate', models.DateTimeField()),
                ('enddate', models.DateTimeField()),
                ('startdate', models.DateTimeField()),
                ('infor', models.TextField(db_index=True, max_length=200)),
                ('status', models.CharField(db_index=True, max_length=5)),
                ('createddate', models.DateTimeField(auto_now_add=True)),
                ('updateddate', models.DateTimeField(auto_now=True)),
                ('idlink', models.PositiveIntegerField(db_index=True)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='VehicleType',
            fields=[
                ('id', models.CharField(serialize=False, max_length=50, primary_key=True)),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField()),
                ('image', models.ImageField(blank=True, upload_to='image/vehicletype/%Y/%m/%d')),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.AlterIndexTogether(
            name='vehicletype',
            index_together=set([('id', 'slug')]),
        ),
        migrations.AlterIndexTogether(
            name='vehiclesupplier',
            index_together=set([('id', 'slug')]),
        ),
        migrations.AddField(
            model_name='vehicleinout',
            name='vehicletype',
            field=models.ForeignKey(related_name='rel_vehio_vehicletypes', to='postage.VehicleType'),
        ),
        migrations.AddField(
            model_name='vehiclecard',
            name='vehiclesupplier',
            field=models.ForeignKey(related_name='rel_vehc_vehiclesuppliers', to='postage.VehicleSupplier'),
        ),
        migrations.AddField(
            model_name='vehiclecard',
            name='vehicletype',
            field=models.ForeignKey(related_name='rel_vehc_vehicletypes', to='postage.VehicleType'),
        ),
        migrations.AddField(
            model_name='vehiclecard',
            name='vehicleuser',
            field=models.ManyToManyField(related_name='rel_vehu_users', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AlterIndexTogether(
            name='cardtype',
            index_together=set([('id', 'slug')]),
        ),
        migrations.AlterIndexTogether(
            name='vehiclecard',
            index_together=set([('cardnumber', 'vehiclenumber')]),
        ),
    ]
