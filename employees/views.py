from braces.views import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, FormView, ListView, DetailView

from employees.forms import MenuHeaderRequestForm
from menu.models import MenuHeader


class EmployeeRegistrationView(CreateView):
    template_name = 'employees/employee/registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('employee_menuheader_list')

    def form_valid(self, form):
        result = super(EmployeeRegistrationView, self).form_valid(form)
        cd = form.cleaned_data
        user = authenticate(username=cd['username'], password=cd['password1'])
        login(self.request, user)
        return result


class EmployeeRequestMenuHeaderView(LoginRequiredMixin, FormView):
    menuheader = None
    form_class = MenuHeaderRequestForm

    def form_valid(self, form):
        self.menuheader = form.cleaned_data['menuheader']
        self.menuheader.employees.add(self.request.user)
        return super(EmployeeRequestMenuHeaderView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('employee_menuheader_detail', args=[self.menuheader.id])


class EmployeeMenuHeaderListView(LoginRequiredMixin, ListView):
    model = MenuHeader
    template_name = 'employees/menuheader/list.html'

    def get_queryset(self):
        qs = super(EmployeeMenuHeaderListView, self).get_queryset()
        return qs.filter(employees__in=[self.request.user])


class EmployeeMenuHeaderDetailView(DetailView):
    model = MenuHeader
    template_name = 'employees/menuheader/detail.html'

    def get_queryset(self):
        qs = super(EmployeeMenuHeaderDetailView, self).get_queryset()
        return qs.filter(employees__in=[self.request.user])

    def get_context_data(self, **kwargs):
        context = super(EmployeeMenuHeaderDetailView, self).get_context_data(**kwargs)
        # get course object
        menuheader = self.get_object()
        if 'menudetail_id' in self.kwargs:
            # get current module
            context['menudetail'] = menuheader.rel_menu_details.get(id=self.kwargs['menudetail_id'])
        else:
            # get first module
            context['menudetail'] = menuheader.rel_menu_details.all()[0]
        return context
