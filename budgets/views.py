from braces.views import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView, ListView

from budgets.models import Tasklist,  Sites #, Profits, Revenues
from menu.models import MenuHeader


class BudgetListView(LoginRequiredMixin, ListView):
    model = MenuHeader
    template_name = 'budgets/menuheader/list.html'

    def get_queryset(self):
        qs = super(BudgetListView, self).get_queryset()
        return qs.filter(employees__in=[self.request.user])


class BudgetDetailView(DetailView):
    model = MenuHeader
    tasklists = Tasklist.objects.all()
    sites = Sites.objects.all()
    #sites.refresh_from_db()
    #revenues = Revenues.objects.all()
    template_name = 'budgets/menuheader/detail.html'
    print('0')

    def get_queryset(self):
        qs = super(BudgetDetailView, self).get_queryset()
        print('11111')
        return qs.filter(employees__in=[self.request.user])

    def get_context_data(self, **kwargs):
        context = super(BudgetDetailView, self).get_context_data(**kwargs)
        # get course object
        menuheader = self.get_object()

        if 'menudetail_id' in self.kwargs:
            # get current module

            context['menudetail'] = menuheader.rel_menu_details.get(id=self.kwargs['menudetail_id'])
            context['tasklists'] = self.tasklists
            context['sites'] = self.get_queryset(self.sites)
            #context['revenues'] = self.revenues
        else:
            # get first module
            context['menudetail'] = menuheader.rel_menu_details.all()[0]
            context['tasklists'] = self.tasklists
            #context['revenues'] = self.revenues
        return context