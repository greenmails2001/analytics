from django.contrib import admin

# Register your models here.
from django.db import models
from django.forms import Textarea

from biapp.models import ChartType, DataType, ColumnList, Combine


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
    list_display = ['id','name', 'slug', 'image', 'description']
    prepopulated_fields = {'slug': ('name',)}
    formfield_overrides = {
        models.TextField: {'widget': Textarea(
                           attrs={'rows': 1,
                                  'cols': 40,
                                  'style': 'height: 5em;'})},
    }

@admin.register(ColumnList)
class ColumnListAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'slug', 'description']
    prepopulated_fields = {'slug': ('name',)}
    formfield_overrides = {
        models.TextField: {'widget': Textarea(
                           attrs={'rows': 1,
                                  'cols': 40,
                                  'style': 'height: 5em;'})},
    }

admin.site.register(Combine)