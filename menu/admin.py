from django.contrib import admin

# Register your models here.
from django.db import models
from django.forms import Textarea

from menu.models import MenuFunction, MenuDetail, MenuHeader, ChartType, MenuDetailEmployees, DataType


@admin.register(MenuFunction)
class MenuFunctionAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug','orderview']
    prepopulated_fields = {'slug': ('name',)}


class MenuDetailInline(admin.TabularInline):
    model = MenuDetail


@admin.register(MenuHeader)
class MenuHeaderAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'orderview', 'menufunction', 'createddate', 'updateddate', 'available']
    list_filter = ['createddate', 'menufunction']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    formfield_overrides = {
        models.TextField: {'widget': Textarea(
                           attrs={'rows': 1,
                                  'cols': 40,
                                  'style': 'height: 5em;'})},
    }
    inlines = [MenuDetailInline]


@admin.register(ChartType)
class ChartTypeAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'slug', 'description']
    prepopulated_fields = {'slug': ('name',)}
    formfield_overrides = {
        models.TextField: {'widget': Textarea(
                           attrs={'rows': 1,
                                  'cols': 40,
                                  'style': 'height: 5em;'})},
    }


@admin.register(DataType)
class DataTypeAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'slug','image','description']
    prepopulated_fields = {'slug': ('name',)}
    formfield_overrides = {
        models.TextField: {'widget': Textarea(
                           attrs={'rows': 1,
                                  'cols': 40,
                                  'style': 'height: 5em;'})},
    }


#Inline phải đặt trước ModelAdmin
#@admin.register(MenuDetailEmployeesInline)
class MenuDetailEmployeesInline(admin.TabularInline):
    model = MenuDetailEmployees


@admin.register(MenuDetail)
class MenuDetailAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'orderview', 'menuheader', 'createddate', 'updateddate', 'available']
    list_filter = ['createddate', 'menuheader']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    formfield_overrides = {
        models.TextField: {'widget': Textarea(
                           attrs={'rows': 1,
                                  'cols': 40,
                                  'style': 'height: 5em;'})},
    }
    inlines = [MenuDetailEmployeesInline]
