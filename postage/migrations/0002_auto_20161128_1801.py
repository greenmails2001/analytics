# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('postage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisteredVehicle',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
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
                ('cardtype', models.ForeignKey(to='postage.CardType', related_name='rel_vehc_cardtypes')),
                ('vehiclesupplier', models.ForeignKey(to='postage.VehicleSupplier', related_name='rel_vehc_vehiclesuppliers')),
                ('vehicletype', models.ForeignKey(to='postage.VehicleType', related_name='rel_vehc_vehicletypes')),
                ('vehicleuser', models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='rel_vehu_users', blank=True)),
            ],
            options={
                'ordering': ('cardnumber',),
            },
        ),
        migrations.AlterIndexTogether(
            name='vehiclecard',
            index_together=set([]),
        ),
        migrations.RemoveField(
            model_name='vehiclecard',
            name='cardtype',
        ),
        migrations.RemoveField(
            model_name='vehiclecard',
            name='vehiclesupplier',
        ),
        migrations.RemoveField(
            model_name='vehiclecard',
            name='vehicletype',
        ),
        migrations.RemoveField(
            model_name='vehiclecard',
            name='vehicleuser',
        ),
        migrations.AddField(
            model_name='vehicleinout',
            name='amount',
            field=models.DecimalField(null=True, decimal_places=6, blank=True, max_digits=20),
        ),
        migrations.AddField(
            model_name='vehicleinout',
            name='charge',
            field=models.DecimalField(null=True, decimal_places=6, blank=True, max_digits=20),
        ),
        migrations.AddField(
            model_name='vehicleinout',
            name='payin',
            field=models.DecimalField(null=True, decimal_places=6, blank=True, max_digits=20),
        ),
        migrations.DeleteModel(
            name='VehicleCard',
        ),
        migrations.AlterIndexTogether(
            name='registeredvehicle',
            index_together=set([('cardnumber', 'vehiclenumber')]),
        ),
    ]
