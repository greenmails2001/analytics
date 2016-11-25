from braces.views import LoginRequiredMixin, PermissionRequiredMixin
from django.apps import apps
from django.core.urlresolvers import reverse_lazy
from django.db.models import Count
from django.forms import modelform_factory
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.views.generic.base import TemplateResponseMixin, View

from budgets.models import Sites, Profits
from budgets.models import Tasklist, Revenues
from employees.forms import MenuHeaderRequestForm
from menu import forms
from menu.forms import MenuDetailFormSet
from menu.models import MenuFunction, MenuHeader, MenuDetail, ItemContent


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
        return qs.filter(owner=self.request.user)


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
        print('refresh trangxxxx %s' %{qs})
        return qs#.filter(employees__in=[self.request.user])

    def get_context_data(self, **kwargs):
        context = super(MainMenuListView, self).get_context_data( **kwargs)
        # get course object
        #menufunction = self.get_object()
        #context['menufunction'] = menufunction
        print('get_context_data 1')
        menufunctions = MenuFunction.objects.annotate(total_menuheaders=Count('rel_menu_headers_functions'))
        menuheaders = MenuHeader.objects.annotate(total_menudetails=Count('rel_menu_details'))

        if 'slug' in self.kwargs:
            print('get_context_data 2')
            menufunction = MenuFunction.objects.get(slug=self.kwargs['slug'])
            menuheaders = menuheaders.filter(menufunction=menufunction)

            print('1.menufunc slug %s' %{menufunction.slug} )

            if 'menuheader_id' in self.kwargs:
                menuheader = MenuHeader.objects.get(id=self.kwargs['menuheader_id'])
                print('2.menuheader %s' %{menuheader.id} )

                if 'menudetail_id' in self.kwargs:
                    # get current module
                    menudetail = menuheader.rel_menu_details.get(id=self.kwargs['menudetail_id'])
                    print('3.menudetail id %s' %{menudetail.id} )

                else:
                    print('7')
                    # get first module
                    menudetail = menuheader.rel_menu_details.all()[0]
                    print('4.menudetail id %s' %{menudetail.id} )
            else:
                print('5')
                menuheader = menuheaders.filter(menufunction=menufunction).first()
                menudetail = menuheader.rel_menu_details.first()
                print('5.menuheader %s' %{menuheader} )
                print('6.menudetail id %s' %{menudetail} )
        context['menufunctions'] = menufunctions
        context['menuheaders'] = menuheaders
        context['menufunction'] = menufunction
        context['menuheader'] = menuheader
        context['menudetail'] = menudetail
        return context


class MenuHeaderDetailView(DetailView):
    model = MenuHeader
    template_name = 'menu/menuheader/detail.html'

    def get_context_data(self, **kwargs):
        context = super(MenuHeaderDetailView, self).get_context_data(**kwargs)
        context['enroll_form'] = MenuHeaderRequestForm(initial={'menuheader':self.object})
        return context


def plotResults(request,site_id):
    #arg=siteid
    import matplotlib
    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    from matplotlib.dates import DateFormatter
    fig = Figure()

    site=get_object_or_404(Sites,siteid=site_id)
    print('plot %s' % site.sitename)
    ax=fig.add_subplot(1,1,1)
    #p = get_object_or_404(Profits, sitename = '124_Villa-Park') # Get the poll object from django
    profits = Profits.objects.filter(sitename=site.sitename)
    numTests = profits.count()
    x = matplotlib.numpy.arange(1,numTests)

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

    #ax.grid(True)
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