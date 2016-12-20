import os

from braces.views import LoginRequiredMixin, PermissionRequiredMixin
from django.apps import apps
from django.core.urlresolvers import reverse_lazy
from django.db.models import Count
from django.forms import modelform_factory
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect, render_to_response

# Create your views here.
from django.utils.encoding import smart_str
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.views.generic.base import TemplateResponseMixin, View

from analytics import settings
from analytics.settings import MEDIA_ROOT
from budgets.models import Sites, Profits
from budgets.models import Tasklist, Revenues
from employee_groups.models import MenuFunctionGroups, MenuHeaderGroups, MenuDetailGroups
from employees.forms import MenuHeaderRequestForm
from menu import forms
from menu.forms import MenuDetailFormSet, ItemContentForm
from menu.models import MenuFunction, MenuHeader, MenuDetail, ItemContent, MonthlyWeatherByCity


def menufunction_dashboard(request, menufunction_slug=None):
    menufunction = None
    menufunctions = MenuFunction.objects.all()
    menuheaders = MenuHeader.objects.filter(available=True)
    if menufunction_slug:
        menufunction = get_object_or_404(MenuFunction, slug=menufunction_slug)
        menuheaders = menuheaders.filter(menufunction=menufunction)
    return render(request, 'menu/menuheader/dashboard_v3.html',
                  {'menufunction': menufunction,
                    'menufunctions': menufunctions,
                    'menuheaders': menuheaders})


def menuheader_list(request, id, slug):
    menuheader = get_object_or_404(MenuHeader, id=id, slug=slug, available=True)
    return render(request, 'menu/menuheader/list.html',
                  {'menuheader': menuheader})


def menudetail_list(request, id, slug):
    menudetail = get_object_or_404(MenuDetail, id=id, slug=slug, available=True)
    return render(request, 'menu/manage/menudetail/list.html',
                  {'menudetail': menudetail})


def homepage(request):
    return render(request, 'menu/menuheader/index.html')


##mixin
class OwnerMixin(object):
    def get_queryset(self):
        qs = super(OwnerMixin, self).get_queryset()
        return qs.filter(owner=self.request.user)


class OwnerEditMixin(object):
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(OwnerEditMixin, self).form_valid(form)


class OwnerMHMixin(OwnerMixin,LoginRequiredMixin):
    model = MenuHeader
    fields = ['name', 'description','slug', 'orderview', 'menufunction',] #, 'createddate', 'updateddate', 'available']
    success_url = reverse_lazy('manage_menuheader_list')


class OwnerMHEditMixin(OwnerMHMixin, OwnerEditMixin):
    #fields = ['name', 'description', 'slug', 'orderview', 'menufunction', 'createddate', 'updateddate', 'available']
    #success_url = reverse_lazy('manage_menuheader_list')
    template_name = 'menu/manage/menuheader/form.html'


#ke thua mixin vua tao
class ManageMHListView(OwnerMHMixin, ListView):
    #model = MenuHeader
    template_name = 'menu/manage/menuheader/list.html'

    def get_queryset(self):
        qs = super(ManageMHListView, self).get_queryset()
        return qs.filter(owner=self.request.user).order_by('menufunction', 'orderview', 'name')


class MHCreateView(PermissionRequiredMixin, OwnerMHEditMixin, CreateView):
    #pass
    permission_required = 'menu.add_menuheader'

class MHUpdateView(PermissionRequiredMixin, OwnerMHEditMixin, UpdateView):
    #pass
    template_name = 'menu/manage/menuheader/form.html'
    permission_required = 'menu.change_menuheader'

class MHDeleteView(PermissionRequiredMixin,OwnerMHMixin, DeleteView):
    template_name = 'menu/manage/menuheader/delete.html'
    success_url = reverse_lazy('manage_menuheader_list')
    permission_required = 'menu.delete_menuheader'


##########menu: inlineformset_factory
class MenuHeaderDetailUpdateView(TemplateResponseMixin, View):
    template_name = 'menu/manage/menudetail/formset.html'
    menuheader = None

    def get_formset(self, data=None):
        return MenuDetailFormSet(instance=self.menuheader, data=data)

    def dispatch(self, request, pk):
        self.menuheader = get_object_or_404(MenuHeader, id=pk, owner=request.user)
        return super(MenuHeaderDetailUpdateView, self).dispatch(request, pk)

    def get(self, request, *args, **kwargs):
        formset = self.get_formset()
        return self.render_to_response({'menuheader': self.menuheader, 'formset': formset})

    def post(self, request, *args, **kwargs):
        formset = self.get_formset(data=request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('manage_menuheader_list')
        return self.render_to_response({'menuheader': self.menuheader, 'formset': formset})

#############itemcontent - tao & update
class ItemContentCreateUpdateView(TemplateResponseMixin, View):
    menudetail = None
    model = None
    obj = None
    template_name = 'menu/manage/itemcontent/form.html'

    def get_model(self, model_name):
        if model_name in ['text', 'video', 'image', 'file', 'chart', 'profit_table', 'url']:
            return apps.get_model(app_label='menu', model_name=model_name)
        return None

    def get_form(self, model, *args, **kwargs):
        #Form = modelform_factory(model, exclude=['owner', 'orderview', 'createddate', 'updateddate'])
        #loai bỏ tuc la k lấy cac column owner, orderview, create...
        ##field choice for form########
        #Form = modelform_factory(model, form=ItemContentForm)#, exclude=['orderview', 'createddate', 'updateddate'])
        ##field choice for model#######
        Form = modelform_factory(model, exclude=['orderview', 'createddate', 'updateddate'])
        return Form(*args, **kwargs)

    def dispatch(self, request, menudetail_id, model_name, id=None):
        self.menudetail = get_object_or_404(MenuDetail, id=menudetail_id, menuheader__owner=request.user)
        self.model = self.get_model(model_name)
        if id:
            self.obj = get_object_or_404(self.model, id=id, owner=request.user)
        return super(ItemContentCreateUpdateView, self).dispatch(request, menudetail_id, model_name, id)

    def get(self, request, menudetail_id, model_name, id=None):
        form = self.get_form(self.model, instance=self.obj)
        return self.render_to_response({'form': form, 'object': self.obj})

    def post(self, request, menudetail_id, model_name, id=None):
        form = self.get_form(self.model, instance=self.obj, data=request.POST, files=request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner = request.user
            obj.save()
            print("1")
            if not id:
                print("2")
                # new content
                ItemContent.objects.create(menudetail=self.menudetail, item=obj)
                print("3")
            return redirect('menudetail_itemcontent_list', self.menudetail.id)
        print("4")
        return self.render_to_response({'form': form, 'object': self.obj})

########itemcontent - delete
class ItemContentDeleteView(View):
    def post(self, request, id):
        itemcontent = get_object_or_404(ItemContent, id=id, menudetail__menuheader__owner=request.user)
        menudetail = itemcontent.menudetail
        itemcontent.item.delete()
        itemcontent.delete()
        return redirect('menudetail_itemcontent_list', menudetail.id)

######### itemcontent - list
class MenuDetailItemContentListView(TemplateResponseMixin, View):
    template_name = 'menu/manage/menudetail/itemcontent_list.html'

    def get(self, request, menudetail_id):
        menudetail = get_object_or_404(MenuDetail, id=menudetail_id, menuheader__owner=request.user)
        return self.render_to_response({'menudetail': menudetail})

#bỏ, thay bằng: MenuHeaderDetailListView
class MenuHeaderListView(TemplateResponseMixin, View):
    model = MenuHeader
    template_name = 'menu/menuheader/main.html'

    def get(self, request, menufunction=None):
        menufunctions = MenuFunction.objects.annotate(total_menuheaders=Count('rel_menu_headers_functions'))
        menuheaders = MenuHeader.objects.annotate(total_menudetails=Count('rel_menu_details'))
        if menufunction:
            menufunction = get_object_or_404(MenuFunction, slug=menufunction)
            menuheaders = menuheaders.filter(menufunction=menufunction)
        return self.render_to_response({'menufunctions': menufunctions,
                                        'menufunction': menufunction,
                                        'menuheaders': menuheaders})


class MainMenuListView(LoginRequiredMixin,DetailView):
    model = MenuFunction
    template_name = 'menu/menuheader/main.html'
    #main = kết hợp giữa
    #template_name = 'menu/menuheader/list.html' &  #template_name = 'budgets/menuheader/detail.html'
    print('0')

    def get_queryset(self):
        qs = super(MainMenuListView, self).get_queryset()
        print('get_queryset: %s' %{qs})
        listgroup=self.request.user.groups.values_list('id',flat=True)
        menufunctionsgroups = MenuFunctionGroups.objects.filter(group__id__in=listgroup).values('menufunction')
        return qs.filter(id__in=menufunctionsgroups)

    def get_context_data(self, **kwargs):
        context = super(MainMenuListView, self).get_context_data( **kwargs)
        # get course object
        menufunction = self.get_object()
        #context['menufunction'] = menufunction
        print('get_context_data 1 %s' %menufunction)
        listgroup=self.request.user.groups.values_list('id',flat=True)
        #print(listgroup)
        menufunctionsgroups = MenuFunctionGroups.objects.filter(group__in=listgroup).values('menufunction')
        print(menufunctionsgroups)
        #for mf in menufunctionsgroups:
        #    print(mf)
        menufunctions = MenuFunction.objects.filter(id__in=menufunctionsgroups).annotate(total_menuheaders=Count('rel_menu_headers_functions'))
        #print(menufunctions)
        #menuheaders = MenuHeader.objects.annotate(total_menudetails=Count('rel_menu_details'))
        menuheadergroups = MenuHeaderGroups.objects.filter(group__in=listgroup).values('menuheader')
        menuheaders = MenuHeader.objects.filter(id__in=menuheadergroups).annotate(total_menudetails=Count('rel_menu_details'))
        print(menuheaders)
        menudetailgroups = MenuDetailGroups.objects.filter(group__in=listgroup).values('menudetail')
        menudetails = MenuDetail.objects.filter(id__in=menudetailgroups,menuheader__in=menuheaders)
        print(menudetails)
        if 'slug' in self.kwargs:
            print('get_context_data 2')
            #menufunction = MenuFunction.objects.get(slug=self.kwargs['slug'])
            menufunction = menufunctions.get(slug=self.kwargs['slug'])
            #print('1.menufunc slug %s' %{menufunction.slug} )
            #menuheadergroups = MenuHeaderGroups.objects.filter(group__in=listgroup).values('menuheader__name')
            menuheaders = menuheaders.filter(menufunction=menufunction)
            #menudetails = MenuDetail.objects.filter(id__in=menudetailgroups,menuheader__in=menuheaders)

            if 'menuheader_id' in self.kwargs:
                menuheader = menuheaders.get(id=self.kwargs['menuheader_id'])
                #print('2.menuheader %s' %{menuheader.id} )

                if 'menudetail_id' in self.kwargs:
                    # get current module

                    #print(menudetailgroups)
                    #####menudetails = menuheader.rel_menu_details.filter(id__in=menudetailgroups).all()
                    menudetail = menudetails.get(id=self.kwargs['menudetail_id'])
                    #print('3.menudetail id %s' %{menudetail.id})
                    print(self.kwargs['menudetail_id'])
                    if self.kwargs['menudetail_id'] == 19:
                        print(self.kwargs['menudetail_id'])
                        return render('account/register_done.html')
                else:
                    print('7')
                    # get first module
                    #menudetailgroups = MenuDetailGroups.objects.filter(group__in=listgroup).values('menudetail')
                    #print(menudetailgroups)
                    #####menudetails = menuheader.rel_menu_details.filter(id__in=menudetailgroups).all()
                    menudetail = menudetails[0]
                    print('4.menudetail id %s' %{menudetail.id} )
            else:
                print('5')
                menuheader = menuheaders.filter(menufunction=menufunction).first()
                #menudetails = menuheader.rel_menu_details.filter(id__in=menudetailgroups).all()
                menudetails = MenuDetail.objects.filter(id__in=menudetailgroups,menuheader__in=menuheaders).all()
                menudetail = menudetails.first()
                print('5.menuheader %s' %{menuheader} )
                print('6.menudetail id %s' %{menudetail} )
        context['menufunctions'] = menufunctions
        context['menuheaders'] = menuheaders
        context['menufunction'] = menufunction
        context['menuheader'] = menuheader
        context['menudetails'] = menudetails
        context['menudetail'] = menudetail
        return context


class MenuHeaderDetailView(DetailView):
    model = MenuHeader
    template_name = 'menu/menuheader/detail.html'

    def get_context_data(self, **kwargs):
        context = super(MenuHeaderDetailView, self).get_context_data(**kwargs)
        context['enroll_form'] = MenuHeaderRequestForm(initial={'menuheader':self.object})
        return context


def file_serve(request, filename):
    if request.user.is_superuser:
        print('################fileserve:')
        response = HttpResponse()
        url = "protected/" + filename
        print(url)
        response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(filename)
        length = os.path.getsize(MEDIA_ROOT + "protected/" + filename)
        print(length)
        response['Content-Length'] = str(length)
        response['X-Accel-Redirect'] = url
        print(response)
        return response
    else:
        return HttpResponseForbidden("Restricted Access")

######test permission file in media dir
#def has_read_permission(self, request, path):
def has_read_permission(request, path):
    "Only show to authenticated users - extend this as desired"
    # Note this could allow access to paths including ../..
    # Don't use this simple check in production!
    return request.user.is_authenticated()

def serve_private_file(request, path):
    "Simple example of a view to serve private files with xsendfile"
    if has_read_permission( request=request, path=path):
        fullpath = os.path.join(settings.PRIVATE_MEDIA_ROOT, path)
        print('fullpath %s' %fullpath)
        response = HttpResponse()
        response['X-Sendfile'] = fullpath
        print('test')
        return response


def plotResults(request, site_id):
    #arg=siteid
    import matplotlib
    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    from matplotlib.dates import DateFormatter
    fig = Figure(facecolor='white')
    #fig = Figure()
    site=get_object_or_404(Sites,siteid=site_id)
    print('plot %s' % site.sitename)
    ax=fig.add_subplot(1,1,1)
    #p = get_object_or_404(Profits, sitename = '124_Villa-Park') # Get the poll object from django
    profits = Profits.objects.filter(sitename=site.sitename)
    numTests = profits.count()

    prices = [profit.price for profit in profits]
    updates = [profit.update for profit in profits]

    ind = matplotlib.numpy.arange(numTests) # the x locations for the groups

    cols = ['red','orange','yellow','green','blue','purple','indigo']*10

    cols = cols[0:len(ind)]
    ax.bar(ind, prices,color=cols)

    ax.set_xticks(ind + 0.5)
    ax.set_xticklabels(updates)

    ax.set_xlabel("Updates")
    ax.set_ylabel("Prices")

    #ax.set_xticklabels(names)
    #site= '124_Villa-Park'
    title = u"Dynamically Generated: %s" % site.sitename
    ax.set_title(title)
    #fig = Figure(facecolor='white')

    #ax.grid(True)
    fig.autofmt_xdate()
    canvas = FigureCanvas(fig)
    response = HttpResponse(content_type='image/png')

    canvas.print_png(response)
    return response


def search(request):
    query = request.GET['q']
    from django.template import loader
    t = loader.get_template('menu/results.html')
    from django.template import Context
    c = Context({ 'query': query,})
    return HttpResponse(t.render(c))
################################################
################################################
################################################
################################################

def plot_profits_barline1111(request, site_id):
    #arg=siteid
    import numpy as np
    import matplotlib
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure

    #####pandas####
    #import pandas as pd
    import datetime as dt
    import matplotlib.dates as md

    fig = plt.Figure()
    #fig = plt.Figure(facecolor='white' )
        #,dpi=200: càng nhỏ ảnh càng mờ:vidu 10 rất mờ.
        #figsize=(20,10)
    ax=fig.add_subplot(1,1,1)#grid 2row x 1col , vitri thu 1
    #figsize=(20, 10)
    print('0')
    site=get_object_or_404(Sites, siteid=site_id)
    print('plot %s' % site.sitename)
    profits = Profits.objects.filter(sitename=site.sitename)
    #dfProfits = pd.DataFrame(list(Profits.objects.all().values()))
    #dfProfitsDate = pd.DataFrame(list(....objects.filter(date__gte=datetime.datetime(2012, 5, 1)).values()))
    ## limit which fields
    #dfProfitsSite = pd.DataFrame(list(....objects.all().values('author', 'date', 'slug')))
    #hoac:
    #dfProfitsSite = pd.DataFrame.from_records(profits)

    prices = [profit.price for profit in profits]
    revenues = [profit.revenue for profit in profits]
    updates = [ profit.update.strftime("%Y-%m-%d(%Hh)") for profit in profits]
    print(updates)
    numTests = profits.count()

    # Set color transparency (0: transparent; 1: solid)
    a = 0.5
    bar_width = 0.35
    opacity = 0.8
    # Remove plot frame
    #ax.set_frame_on(False)
    #plt.subplots_adjust(bottom=0.6,hspace = 0.2)
    #ax.title.set_position((0.1,1.08))#(x,y) x chay tu trái sang phải 0.1->1.1 , y chay tu dưới lên trên: 0.1->1.1
    ind = matplotlib.numpy.arange(numTests) # the x locations for the groups
    print('2')
    ax.bar(ind, prices, bar_width,
                 alpha=a,
                 color='b',
                 label='Price')
    ax.bar(ind + bar_width, revenues, bar_width,
                 alpha=opacity,
                 color='g',
                 label='Revenue')
    print('3')

    ax.set_xlabel('Time')
    print('3.1')
    ax.set_ylabel('($)')
    print('3.2')
    ax.set_title('Revenue, Expense by Date.')
    print('3.3')

    #updates_n = matplotlib.dates.date2num(updates)
    ax.set_xticks(ind + bar_width/2)
    ax.set_xticklabels(  updates, rotation=90, size=10)
    #xfmt = md.DateFormatter('%Y-%m-%d\n%H:$M:%S')
    #ax.xaxis.set_major_formatter(xfmt)
    ax.legend()
    print('4')
    #ax.grid(True)

    fig.autofmt_xdate()
    canvas = FigureCanvas(fig)
    response = HttpResponse(content_type='image/png')
    canvas.print_png(response)

    return response


def plot_profits_barline2222(request, site_id):
    import numpy as np
    import matplotlib
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure

    #####pandas####
    #import pandas as pd
    import datetime as dt
    import matplotlib.dates as md

    fig = plt.Figure(figsize=(7,14))
    #fig = plt.Figure(facecolor='white',figsize=(7,14) )
        #,dpi=200: càng nhỏ ảnh càng mờ:vidu 10 rất mờ.
        #figsize=(20,10)
    ax=fig.add_subplot(1,1,1)#211: grid 2row x 1col , vitri thu 1
    #figsize=(20, 10)
    print('0')
    site=get_object_or_404(Sites, siteid=site_id)
    print('plot %s' % site.sitename)
    profits = Profits.objects.filter(sitename=site.sitename)

    print('1.1')
    prices = [profit.price for profit in profits]
    priceupts = [profit.priceupt for profit in profits]
    print('1.2')
    revenues = [profit.revenue for profit in profits]
    revenueupts = [profit.revenueupt for profit in profits]
    print('1.3')
    updates = [ profit.update.strftime("%Y-%m-%d(%Hh)") for profit in profits]

    print(updates)

    numTests = profits.count()

    # Set color transparency (0: transparent; 1: solid)
    bar_width = 0.35
    opacity = 0.8
    # Remove plot frame
    #ax.set_frame_on(False)
    #plt.subplots_adjust(bottom=0.6,hspace = 0.2)
    #ax.title.set_position((0.1,1.08))#(x,y) x chay tu trái sang phải 0.1->1.1 , y chay tu dưới lên trên: 0.1->1.1
    ind = matplotlib.numpy.arange(numTests) # the x locations for the groups
    print('2')
    ax.bar(ind, prices, bar_width,
                 alpha=opacity,
                 color='b',
                 label='Price')
    ax.bar(ind + bar_width, revenues, bar_width,
                 alpha=opacity,
                 color='g',
                 label='Revenue')
    ax.plot(ind+bar_width/2.,  priceupts,color='r', label='Price Upt')
    ax.scatter(ind+bar_width/2.,  priceupts,color='r')

    ax.plot(ind+bar_width*3/2.,  revenueupts,color='y', label='Revenue Upt')
    ax.scatter(ind+bar_width*3/2.,  revenueupts,color='y')
    print('3')

    ax.set_xlabel('Time')
    print('3.1')
    ax.set_ylabel('($)')
    print('3.2')
    ax.set_title('Revenue, Expense by Date.')
    print('3.3')

    #updates_n = matplotlib.dates.date2num(updates)
    ax.set_xticks(ind + bar_width/2)
    ax.set_xticklabels(updates, rotation=90, size=10)
    ax.legend()
    print('4')
    #ax.grid(True)

    fig.autofmt_xdate()
    canvas = FigureCanvas(fig)
    response = HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response

####fail, chưa chay dc
def plot_profits_barline33333(request, site_id):
    import numpy as np
    import matplotlib
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure

    #####pandas####
    #import pandas as pd
    import datetime as dt
    import matplotlib.dates as md

    fig = plt.Figure()
    #fig = plt.Figure(facecolor='white',figsize=(7,14) )
        #,dpi=200: càng nhỏ ảnh càng mờ:vidu 10 rất mờ.
        #figsize=(20,10)
    #ax=fig.add_subplot(1,1,1)#211: grid 2row x 1col , vitri thu 1
    #figsize=(20, 10)
    print('0')
    site=get_object_or_404(Sites, siteid=site_id)
    print('plot %s' % site.sitename)
    profits = Profits.objects.filter(sitename=site.sitename)

    print('1.1')
    prices = [profit.price for profit in profits]
    priceupts = [profit.priceupt for profit in profits]
    print('1.2')
    revenues = [profit.revenue for profit in profits]
    revenueupts = [profit.revenueupt for profit in profits]
    print('1.3')
    updates = [ profit.update.strftime("%Y-%m-%d(%Hh)") for profit in profits]

    print(updates)

    numTests = profits.count()

    # Set color transparency (0: transparent; 1: solid)
    bar_width = 0.35
    opacity = 0.8
    # Remove plot frame
    #ax.set_frame_on(False)
    #plt.subplots_adjust(bottom=0.6,hspace = 0.2)
    #ax.title.set_position((0.1,1.08))#(x,y) x chay tu trái sang phải 0.1->1.1 , y chay tu dưới lên trên: 0.1->1.1
    ind = matplotlib.numpy.arange(numTests) # the x locations for the groups
    print('2')
    plt.bar(ind, prices, bar_width,
                 alpha=opacity,
                 color='b',
                 label='Price')
    plt.bar(ind + bar_width, revenues, bar_width,
                 alpha=opacity,
                 color='g',
                 label='Revenue')
    plt.plot(ind+bar_width/2.,  priceupts,color='r', label='Price Upt')
    plt.scatter(ind+bar_width/2.,  priceupts,color='r')

    plt.plot(ind+bar_width*3/2.,  revenueupts,color='y', label='Revenue Upt')
    plt.scatter(ind+bar_width*3/2.,  revenueupts,color='y')
    print('3')

    plt.xlabel('Time')
    print('3.1')
    plt.ylabel('($)')
    print('3.2')
    plt.title('Revenue, Expense by Date.')
    print('3.3')

    #updates_n = matplotlib.dates.date2num(updates)
    plt.xticks(ind + bar_width/2,updates)
    plt.autoscale(tight=True)
    #plt.xticklabels(updates, rotation=90, size=10)
    #plt.legend()
    print('4')
    #ax.grid(True)

    #fig.autofmt_xdate()
    canvas = FigureCanvas(fig)
    print('5')
    response = HttpResponse(content_type='image/png')
    canvas.print_png(response)
    print('6')

    return response

