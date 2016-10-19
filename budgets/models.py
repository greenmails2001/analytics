from django.db import models

# Create your models here.
#from __future__ import unicode_literals

class Sites(models.Model):
    siteid = models.TextField(db_column='SiteID', primary_key=True)  # Field name made lowercase.
    sitename = models.TextField(db_column='SiteName', blank=True, null=True)  # Field name made lowercase.
    manager = models.TextField(db_column='Manager', blank=True, null=True)  # Field name made lowercase.
    phone = models.TextField(db_column='Phone', blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    currentdate = models.DateTimeField(db_column='CurrentDate', blank=True, null=True)  # Field name made lowercase.
    finished = models.CharField(db_column='Finished', max_length=1, blank=True, null=True)  # Field name made lowercase.
    area = models.DecimalField(db_column='Area', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
    imagelink = models.TextField(db_column='ImageLink', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = True
        db_table = 'sites'


class Tasklist(models.Model):
    taskid = models.TextField(db_column='TaskID', primary_key=True)  # Field name made lowercase.
    shortname = models.TextField(db_column='ShortName', blank=True, null=True)  # Field name made lowercase.
    taskname = models.TextField(db_column='TaskName', blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = True
        db_table = 'tasklist'


class TestProfits(models.Model):
    profitid = models.PositiveIntegerField(db_column='ProfitID', primary_key=True)
    taskid = models.TextField(db_column='TaskID')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    update = models.DateTimeField(db_column='Update')  # Field name made lowercase.
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    priceupt = models.FloatField(db_column='PriceUpt', blank=True, null=True)  # Field name made lowercase.
    priceact = models.FloatField(db_column='PriceAct', blank=True, null=True)  # Field name made lowercase.
    sitename = models.TextField(db_column='SiteName')  # Field name made lowercase.
    revenue = models.FloatField(db_column='Revenue', blank=True, null=True)  # Field name made lowercase.
    revenueupt = models.FloatField(db_column='RevenueUpt', blank=True, null=True)  # Field name made lowercase.
    revenueact = models.FloatField(db_column='RevenueAct', blank=True, null=True)  # Field name made lowercase.
    profit = models.FloatField(db_column='Profit', blank=True, null=True)  # Field name made lowercase.
    profitupt = models.FloatField(db_column='ProfitUpt', blank=True, null=True)  # Field name made lowercase.
    profitact = models.FloatField(db_column='ProfitAct', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = True
        db_table = 'testprofits'
        unique_together = (('taskid', 'update', 'sitename'),)