from django.contrib import admin

# Register your models here.
from menu.models import MenuFunction, MenuDetail, MenuHeader, ChartType, MenuDetailEmployees


@admin.register(MenuFunction)
class MenuFunctionAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class MenuDetailInline(admin.TabularInline):
    model = MenuDetail


@admin.register(MenuHeader)
class MenuHeaderAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'orderview', 'menufunction', 'createddate', 'updateddate', 'available']
    list_filter = ['createddate', 'menufunction']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [MenuDetailInline]


@admin.register(ChartType)
class ChartTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug','description']
    prepopulated_fields = {'slug': ('name',)}

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
    inlines = [MenuDetailEmployeesInline]



