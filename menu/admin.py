from django.contrib import admin

# Register your models here.
from menu.models import MenuFunction, MenuDetail, MenuHeader


@admin.register(MenuFunction)
class MenuFunctionAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class MenuDetailInline(admin.StackedInline):
    model = MenuDetail


@admin.register(MenuHeader)
class MenuHeaderAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'orderview', 'menufunction', 'createddate', 'updateddate', 'available']
    list_filter = ['createddate', 'menufunction']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [MenuDetailInline]