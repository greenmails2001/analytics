
from braces.views import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.views.generic import DetailView, ListView


from budgets.models import Tasklist,  Sites, Profits, Revenues  #, Profits, Revenues
from menu.models import MenuHeader


class BudgetListView(LoginRequiredMixin, ListView):
    model = MenuHeader
    template_name = 'budgets/menuheader/list.html'

    def get_queryset(self):
        qs = super(BudgetListView, self).get_queryset()
        return qs.filter(employees__in=[self.request.user])


class BudgetDetailView(DetailView):
    model = MenuHeader
    template_name = 'budgets/menuheader/detail.html'
    print('0')

    def get_queryset(self):
        qs = super(BudgetDetailView, self).get_queryset()
        print('refresh trang')
        return qs.filter(employees__in=[self.request.user])

    def get_context_data(self, **kwargs):
        context = super(BudgetDetailView, self).get_context_data( **kwargs)
        # get course object
        menuheader = self.get_object()
        print('2')
        tasklists = Tasklist.objects.all()
        sites = Sites.objects.all()
        revenues= Revenues.objects.all()
        profits = Profits.objects.all()
        print('3')
        if 'menudetail_id' in self.kwargs:
            # get current module
            print('4')
            context['menudetail'] = menuheader.rel_menu_details.get(id=self.kwargs['menudetail_id'])
            if 'site_id' in self.kwargs:
                print('5')
                psite = Sites.objects.get(siteid=self.kwargs['site_id'])
                context['psite'] = psite
                print(psite.sitename)
                context['profits'] = Profits.objects.filter(sitename=psite.sitename) #profits
            else:
                print('6')
                context['psite'] = sites[0]
                print(sites[0].sitename)
                context['profits'] = profits
                print(profits[0].taskid)
            context['tasklists'] = tasklists
            context['sites'] = sites
            context['revenues'] = revenues
        else:
            print('7')
            # get first module
            context['menudetail'] = menuheader.rel_menu_details.all()[0]
            context['psite'] = sites[0]
            context['tasklists'] = tasklists
            context['sites'] = sites
            context['profits'] = profits
            context['revenues'] = revenues
        return context


def grafico (rquest):
    from django.shortcuts import render
    from matplotlib import pylab

    import PIL
    import PIL.Image
    import io
    #from io import *
    import PIL, PIL.Image
    from django.utils.six import StringIO
    from numpy import arange,sin, pi
    from matplotlib.pyplot import plot
    from matplotlib.pyplot import xlabel
    from matplotlib.pyplot import ylabel
    from matplotlib.pyplot import title
    from matplotlib.pyplot import grid
    pos = arange(10)+ 2

    from matplotlib.pyplot import barh
    barh(pos,(1,2,3,4,5,6,7,8,9,10), align = 'center')

    from matplotlib.pyplot import yticks
    yticks(pos,('#hcsm','#ukmedlibs','#ImmunoChat','#HCLDR','#ICTD2015','#hpmglobal','#BRCA','#BCSM','#BTSM','#OTalk'))

    xlabel('Popularidad')
    ylabel('Hashtags')
    title('Gráfico de Hashtags')
    from matplotlib.pyplot import subplots_adjust
    subplots_adjust(left=0.21)

    buffer = io.BytesIO()
    canvas = pylab.get_current_fig_manager().canvas
    canvas.draw()
    graphIMG = PIL.Image.fromstring('RGB', canvas.get_width_height(), canvas.tostring_rgb())
    graphIMG.save(buffer, "PNG")
    pylab.close()
    return HttpResponse (buffer.getvalue(), content_type="Image/png")


def showimage(request):
    from django.http import HttpResponse
    from matplotlib import pylab

    import PIL, PIL.Image
    from django.utils.six import StringIO
    from numpy import arange,sin, pi
    from matplotlib.pyplot import plot
    from matplotlib.pyplot import xlabel
    from matplotlib.pyplot import ylabel
    from matplotlib.pyplot import title
    from matplotlib.pyplot import grid

    # Construct the graph
    t = arange(0.0, 2.0, 0.01)
    s = sin(2*pi*t)

    plot(t, s, linewidth=1.0)
    xlabel('time (s)')
    ylabel('voltage (mV)')
    title('About as simple as it gets, folks')
    grid(True)
    # Store image in a string buffer
    buffer = StringIO.StringIO()
    canvas = pylab.get_current_fig_manager().canvas
    canvas.draw()
    pilImage = PIL.Image.fromstring("RGB", canvas.get_width_height(), canvas.tostring_rgb())
    pilImage.save(buffer, "PNG")
    pylab.cose()

    # Send buffer in a http response the the browser with the mime type image/png set
    return HttpResponse(buffer.getvalue(), mimetype="image/png")


def plotResults(request):
    #arg=siteid
    import matplotlib
    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    from matplotlib.dates import DateFormatter
    fig = Figure()

    ax=fig.add_subplot(1,1,1)
    #p = get_object_or_404(Profits, sitename = '124_Villa-Park') # Get the poll object from django
    profits = Profits.objects.filter(sitename='124_Villa-Park')
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
    site= '124_Villa-Park'
    title = u"Dynamically Generated Results Plot for poll: %s" %site
    ax.set_title(title)

    #ax.grid(True)
    canvas = FigureCanvas(fig)
    response = HttpResponse(content_type='image/png')

    canvas.print_png(response)
    return response