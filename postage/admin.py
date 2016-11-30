# Register your models here.
from django.contrib import admin
from django.db import models
from django.forms import Textarea

from postage.models import CardType, VehicleType, VehicleSupplier, VehicleInOut, RegisteredVehicle


@admin.register(CardType)
class CardTypeAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'slug','description','orderview']
    list_editable = ['id','name', 'slug','description','orderview']
    prepopulated_fields = {'slug': ('id',)}
    ##resize textfield, binh thuong textfield quá cao k phù hợp.
    formfield_overrides = {
        models.TextField: {'widget': Textarea(
                           attrs={'rows': 1,
                                  'cols': 40,
                                  'style': 'height: 5em;'})},
    }

#class MenuDetailInline(admin.TabularInline):
#    model = MenuDetail


@admin.register(VehicleType)
class VehicleTypeAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'slug','description','orderview']
    list_editable = ['id','name', 'slug','description','orderview']
    list_filter = ['id','name']
    search_fields = ['id','name']
    prepopulated_fields = {'slug': ('id',)}
    ##resize textfield, binh thuong textfield quá cao k phù hợp.
    formfield_overrides = {
        models.TextField: {'widget': Textarea(
                           attrs={'rows': 1,
                                  'cols': 40,
                                  'style': 'height: 5em;'})},
    }

@admin.register(VehicleSupplier)
class VehicleSupplierAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'slug','slotnumber','orderview','registerdate','enddate','startdate','status','infor','idlink','createddate','updateddate']
    list_editable= ['id','name', 'slug','slotnumber','orderview','registerdate','enddate','startdate','status','infor','idlink']
    list_filter = ['id','name','status']
    search_fields = ['id','name','status']
    prepopulated_fields = {'slug': ('id',)}
    ##resize textfield, binh thuong textfield quá cao k phù hợp.
    formfield_overrides = {
        models.TextField: {'widget': Textarea(
                           attrs={'rows': 1,
                                  'cols': 40,
                                  'style': 'height: 5em;'})},
        models.CharField: {'widget': Textarea(
                           attrs={'rows': 1,
                                  'cols': 10,
                                  'style': 'height: 1.5em;'})},
    }


@admin.register(VehicleInOut)
class VehicleInOutAdmin(admin.ModelAdmin):
    list_display = ['id','cardtype', 'vehicletype','vehiclenumber','checkin','checkout','stationnamein','stationnameout',
                    'status','idlink','amount','payin','charge']
    list_editable= ['id','cardtype', 'vehicletype','vehiclenumber','checkin','checkout','stationnamein','stationnameout',
                    'status','idlink','amount','payin','charge']
    list_filter = ['id','cardtype','vehicletype','vehiclenumber','status']
    search_fields = ['id','cardtype','vehicletype','vehiclenumber','status']
    #prepopulated_fields = {'slug': ('id',)}
    ##resize textfield, binh thuong textfield quá cao k phù hợp.
    formfield_overrides = {
        models.TextField: {'widget': Textarea(
                           attrs={'rows': 1,
                                  'cols': 40,
                                  'style': 'height: 5em;'})},
        models.CharField: {'widget': Textarea(
                           attrs={'rows': 1,
                                  'cols': 10,
                                  'style': 'height: 1.5em;'})},
    }


@admin.register(RegisteredVehicle)
class RegisteredVehicleAdmin(admin.ModelAdmin):
    list_display = ['id','cardnumber','cardtype', 'vehicletype','vehicleowner','vehicleuser','vehiclesupplier','vehiclenumber',
                    'registerdate','enddate','startdate','infor', 'status','idlink']
    list_editable= ['id','cardnumber','cardtype', 'vehicletype','vehicleowner','vehicleuser','vehiclesupplier','vehiclenumber',
                    'registerdate','enddate','startdate','infor', 'status','idlink']
    list_filter = ['id','cardtype','vehicletype','vehiclenumber','cardnumber','status']
    search_fields = ['id','cardtype','vehicletype','vehiclenumber','cardnumber','status']
    #prepopulated_fields = {'slug': ('id',)}
    ##resize textfield, binh thuong textfield quá cao k phù hợp.
    formfield_overrides = {
        models.TextField: {'widget': Textarea(
                           attrs={'rows': 1,
                                  'cols': 40,
                                  'style': 'height: 5em;'})},
        models.CharField: {'widget': Textarea(
                           attrs={'rows': 1,
                                  'cols': 10,
                                  'style': 'height: 1.5em;'})},
    }

