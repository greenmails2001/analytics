# Register your models here.
from django.contrib import admin

# Register your models here.
from django.db import models
from django.forms import Textarea

from budgets.models import Budgets, Profits, Revenues, Sites, Tasklist


@admin.register(Budgets)
class BudgetsAdmin(admin.ModelAdmin):
    #models=Budgets
    list_display = ['taskid', 'taskname','update','unit','qty','unitprice','price','note','reason',
                    'qtyupt','unitpriceupt','priceupt','noteupt','reasonupt','qtyact','priceact','noteact',
                    'siteid']
    list_editable = ['taskid', 'taskname','update','unit','qty','unitprice','price','note','reason',
                    'qtyupt','unitpriceupt','priceupt','noteupt','reasonupt','qtyact','priceact','noteact',
                    'siteid']
    search_fields = ['siteid','taskid',]
    list_filter = ['siteid','update',]
    #prepopulated_fields = {'slug': ('name',)}
    formfield_overrides = {
        models.TextField: {'widget': Textarea(
                           attrs={'rows': 1,
                                  'cols': 30,
                                  'style': 'height: 4em;'})},
    }


@admin.register(Profits)
class ProfitsAdmin(admin.ModelAdmin):
    models=Profits
    #list_display = ['name', 'slug','orderview']
    #prepopulated_fields = {'slug': ('name',)}


@admin.register(Revenues)
class RevenuesAdmin(admin.ModelAdmin):
    models=Revenues


@admin.register(Tasklist)
class TasklistAdmin(admin.ModelAdmin):
    models=Tasklist


#class BudgetsInline(admin.TabularInline):
#    model = Budgets

#class ProfitsInline(admin.TabularInline):
#    model = Profits

#class RevenuesInline(admin.TabularInline):
#    model = Revenues

@admin.register(Sites)
class SitesAdmin(admin.ModelAdmin):
    models=Sites
    #inlines = [BudgetsInline,ProfitsInline,RevenuesInline]
