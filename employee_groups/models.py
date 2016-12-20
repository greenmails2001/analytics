from django.contrib.auth.models import Group
from django.db import models

# Create your models here.
###group permission###############
from menu.models import MenuFunction, MenuHeader, MenuDetail, ItemContent


class MenuFunctionGroups(models.Model):
    menufunction = models.ForeignKey(MenuFunction, related_name='rel_mfgs_mfs')
    group = models.ForeignKey(Group, related_name='rel_mfgs_groups')
    description = models.TextField(max_length=200,blank=True)
    available = models.BooleanField(default=True)
    createddate = models.DateTimeField(auto_now_add=True)
    updateddate = models.DateTimeField(auto_now=True)

class MenuHeaderGroups(models.Model):
    menuheader = models.ForeignKey(MenuHeader, related_name='rel_mhgs_mhs')
    group = models.ForeignKey(Group, related_name='rel_mhgs_groups')
    description = models.TextField(max_length=200,blank=True)
    available = models.BooleanField(default=True)
    createddate = models.DateTimeField(auto_now_add=True)
    updateddate = models.DateTimeField(auto_now=True)

class MenuDetailGroups(models.Model):
    menudetail = models.ForeignKey(MenuDetail, related_name='rel_mdgs_mds')
    group = models.ForeignKey(Group, related_name='rel_mdgs_groups')
    description = models.TextField(max_length=200,blank=True)
    available = models.BooleanField(default=True)
    createddate = models.DateTimeField(auto_now_add=True)
    updateddate = models.DateTimeField(auto_now=True)

class ItemContentGroups(models.Model):
    itemcontent = models.ForeignKey(ItemContent, related_name='rel_ictgs_icts')
    group = models.ForeignKey(Group, related_name='rel_ictgs_groups')
    description = models.TextField(max_length=200,blank=True)
    available = models.BooleanField(default=True,db_index=True)
    createddate = models.DateTimeField(auto_now_add=True)
    updateddate = models.DateTimeField(auto_now=True)
