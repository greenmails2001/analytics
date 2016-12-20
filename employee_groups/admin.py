from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.models import Group
from django.db import models
from django.forms import Textarea

from employee_groups.models import MenuDetailGroups, MenuHeaderGroups, MenuFunctionGroups, ItemContentGroups

admin.site.unregister(Group)

class MenuFunctionGroupsInline(admin.TabularInline):
    model = MenuFunctionGroups
    extra = 1
    formfield_overrides = {
        models.TextField: {'widget': Textarea(
                           attrs={'rows': 1,
                                  'cols': 30,
                                  'style': 'height: 4em;'})},
    }

class MenuHeaderGroupsInline(admin.TabularInline):
    model = MenuHeaderGroups
    extra = 1
    formfield_overrides = {
        models.TextField: {'widget': Textarea(
                           attrs={'rows': 1,
                                  'cols': 30,
                                  'style': 'height: 4em;'})},
    }

class MenuDetailGroupsInline(admin.TabularInline):
    model = MenuDetailGroups
    extra = 1
    formfield_overrides = {
        models.TextField: {'widget': Textarea(
                           attrs={'rows': 1,
                                  'cols': 30,
                                  'style': 'height: 4em;'})},
    }

class ItemContentGroupsInline(admin.TabularInline):
    model = ItemContentGroups
    extra = 1
    formfield_overrides = {
        models.TextField: {'widget': Textarea(
                           attrs={'rows': 1,
                                  'cols': 30,
                                  'style': 'height: 4em;'})},
    }

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    models=Group
   # list_display = ['id','name', 'slug','description','orderview']
    #list_editable = ['id','name', 'slug','description','orderview']
    #prepopulated_fields = {'slug': ('id',)}
    ##resize textfield, binh thuong textfield quá cao k phù hợp.
    inlines = [MenuFunctionGroupsInline,MenuHeaderGroupsInline,MenuDetailGroupsInline,ItemContentGroupsInline]

