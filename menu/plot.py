import datetime

from braces.views import LoginRequiredMixin


from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, render_to_response
from django.views.generic import DetailView, View
from django.views.generic.base import TemplateResponseMixin

from budgets.models import Profits, Sites, Revenues, Tasklist, Budgets

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from chartit import DataPool, Chart

#from menu.models import MonthlyWeatherByCity


def autolabel_billion(rects, divide, ax, color, v_axes):
    # attach some text labels
    for rect in rects:
        value = rect.get_height()/float(divide)
        ax.text(rect.get_x() + rect.get_width()/2., 1.0*rect.get_height(),
                '%10.2f' % float(value),
                ha='center', va=v_axes, rotation=0, color=color)#rotation xoay text, va=v_axes='bottom'


def autolabel_dot_billion(x,y, divide, ax, color, v_axes):
    # attach some text labels
    print(x)
    print(y)
    print(len(list(x)))
    for i in range(len(list(x))):
        value = float(y[i])/float(divide)
        print('i,value: {}.{}'.format(i,value))
        #v_axes = 'bottom' if i%2==1 else 'top'
        print('v_axes %s' %v_axes)
        ax.text(x[i], y[i],
                '%10.2f' % float(value),
                ha='center', va=v_axes, rotation=0, color=color)#rotation xoay text, va=v_axes='bottom'


class PlotView(LoginRequiredMixin):
    #model = MenuFunction
    #template_name = 'menu/menuheader/main.html'

    #profit: price, revenue
    def plot_profits_barline(request, site_id):
        fig = Figure(facecolor='white',figsize=(7,10))
        #fig = plt.Figure(facecolor='white',figsize=(7,14) )
            #,dpi=200: càng nhỏ ảnh càng mờ:vidu 10 rất mờ.
            #figsize=(20,10)
        #ax=fig.add_subplot(1,1,1) #(2,1,1) hoac (211) là như nhau: grid 2row x 1col , vitri thu 1
        ##dùng add_axes hieu qua hon, dep hơn, subplot dùng cho multi chart
        ##[x1, y1, x2, y2] -->x1,y1: góc dưới bên trái, x2,y2: góc trên ben phải,
        # bound chạy từ[0->1]
        ax=fig.add_axes([0.1, 0.1, 0.89, 0.85])
        #figsize=(20, 10)
        site=get_object_or_404(Sites, siteid=site_id)
        print('plot %s' % site.sitename)
        profits = Profits.objects.filter(sitename=site.sitename)
        prices = [profit.price for profit in profits]
        priceupts = [profit.priceupt for profit in profits]
        revenues = [profit.revenue for profit in profits]
        revenueupts = [profit.revenueupt for profit in profits]
        updates = [ profit.update.strftime("%Y-%m-%d(%Hh)") for profit in profits]
        numTests = profits.count()

        # Set color transparency (0: transparent; 1: solid)
        bar_width = 0.35
        opacity = 0.4
        # Remove plot frame
        #ax.set_frame_on(False)
        #plt.subplots_adjust(bottom=0.6,hspace = 0.2)
        #ax.title.set_position((0.1,1.08))#(x,y) x chay tu trái sang phải 0.1->1.1 , y chay tu dưới lên trên: 0.1->1.1
        ind = matplotlib.numpy.arange(numTests) # the x locations for the groups
        rects1=ax.bar(ind, prices, bar_width,
                     alpha=opacity,
                     color='#ffc300',
                     label='Price')
        rects2=ax.bar(ind + bar_width, revenues, bar_width,
                     alpha=opacity,
                     color='#ffc3f2',
                     label='Revenue')
        rects3=ax.plot(ind+bar_width/2., priceupts,color='r', label='Price Upt')
        ax.scatter(ind+bar_width/2., priceupts,color='r')

        rects4=ax.plot(ind+bar_width*3/2., revenueupts, color='black', label='Revenue Upt')
        ax.scatter(ind+bar_width*3/2., revenueupts, color='black')

        ax.set_xlabel('Time')
        ax.set_ylabel('($)')
        ax.set_title('Revenue, Expense by Date.')

        #updates_n = matplotlib.dates.date2num(updates)
        ax.set_xticks(ind + bar_width/2)
        ax.set_xticklabels(updates, rotation=90, size=10)
        ax.legend()
        #ax.grid(True)
        autolabel_billion(rects1, 100000000000., ax, 'red', 'bottom')#10^11
        autolabel_billion(rects2, 100000000000., ax, 'black', 'bottom')#10^11
        autolabel_dot_billion(ind + bar_width/2., priceupts, 100000000000., ax, '#ffc300', 'bottom')#10^11
        autolabel_dot_billion(ind + bar_width*3/2., revenueupts , 100000000000., ax, 'green', 'bottom')#10^11

        fig.autofmt_xdate()
        canvas = FigureCanvas(fig)
        response = HttpResponse(content_type='image/png')
        canvas.print_png(response)
        return response

    ##plot_revenues_line
    def plot_revenues_line(request, site_id):
        fig = Figure(facecolor='white',figsize=(7,10))
        #fig = plt.Figure(facecolor='white',figsize=(7,14) )
            #,dpi=200: càng nhỏ ảnh càng mờ:vidu 10 rất mờ.
            #figsize=(20,10)
        #ax=fig.add_subplot(1,1,1) #(2,1,1) hoac (211) là như nhau: grid 2row x 1col , vitri thu 1
        ##dùng add_axes hieu qua hon, dep hơn, subplot dùng cho multi chart
        ##[x1, y1, x2, y2] -->x1,y1: góc dưới bên trái, x2,y2: góc trên ben phải,
        # bound chạy từ[0->1]
        ax=fig.add_axes([0.1, 0.1, 0.89, 0.85])

        #figsize=(20, 10)
        site=get_object_or_404(Sites, siteid=site_id)
        print('plot %s' % site.sitename)
        revenues = Revenues.objects.filter(sitename=site.sitename)
        numTests = revenues.count()

        revs = [revenue.revenue for revenue in revenues]
        revupts = [revenue.revenueupt for revenue in revenues]
        revacts = [revenue.revenueact for revenue in revenues]
        updates = [revenue.update.strftime("%Y-%m-%d(%Hh)") for revenue in revenues]

        # Set color transparency (0: transparent; 1: solid)
        bar_width = 0.35
        opacity = 0.4
        # Remove plot frame
        #ax.set_frame_on(False)
        #plt.subplots_adjust(bottom=0.6,hspace = 0.2)
        #ax.title.set_position((0.1,1.08))#(x,y) x chay tu trái sang phải 0.1->1.1 , y chay tu dưới lên trên: 0.1->1.1
        ind = matplotlib.numpy.arange(numTests) # the x locations for the groups
        rects1=ax.plot(ind, revs, color='b', label='Revenue')
        ax.scatter(ind, revs,color='b')

        #rects2=ax.plot(ind, revupts,color='r', label='Revenue Upt')
        #ax.scatter(ind, revupts,color='r')

        #rects3=ax.plot(ind, revacts, color='black', label='Revenue Act')
        #ax.scatter(ind, revacts, color='black')
        ax.set_xlabel('Time')
        ax.set_ylabel('($)')
        ax.set_title('Revenue by Date.')

        #updates_n = matplotlib.dates.date2num(updates)
        ax.set_xticks(ind)
        ax.set_xticklabels(updates, rotation=90, size=10)
        ax.legend()
        #ax.grid(True)
        autolabel_dot_billion(ind, revs,100000000000. , ax, '#ffc300', 'bottom')#10^11
        #autolabel_dot_billion(ind, revupts,1. , ax, 'y', 'bottom')#10^11
        #autolabel_dot_billion(ind, revacts, 1., ax, 'black', 'bottom')#10^11

        fig.autofmt_xdate()
        canvas = FigureCanvas(fig)
        response = HttpResponse(content_type='image/png')
        canvas.print_png(response)
        return response

    ##plot_profits_line
    def plot_profits_line(request, site_id):
        fig = Figure(facecolor='white',figsize=(15,10))
        #fig = plt.Figure(facecolor='white',figsize=(7,14) )
            #,dpi=200: càng nhỏ ảnh càng mờ:vidu 10 rất mờ.
            #figsize=(20,10)

        #ax=fig.add_subplot(1,1,1) #(2,1,1) hoac (211) là như nhau: grid 2row x 1col , vitri thu 1

        ##dùng add_axes hieu qua hon, dep hơn, subplot dùng cho multi chart
        ##[x1, y1, x2, y2] -->x1,y1: góc dưới bên trái, x2,y2: góc trên ben phải,
        # bound chạy từ[0->1]
        #ax=fig.add_axes([0.1, 0.1, 0.89, 0.85])#tile 1:2
        ax=fig.add_axes([0.1, 0.1, 0.89, 0.85])

        #figsize=(20, 10)
        site=get_object_or_404(Sites, siteid=site_id)
        print('plot %s' % site.sitename)
        profits = Profits.objects.filter(sitename=site.sitename)

        profs = [profit.profit for profit in profits]
        prof_upts = [profit.profitupt for profit in profits]
        prof_acts = [profit.profitact for profit in profits]
        updates = [profit.update.strftime("%Y-%m-%d(%Hh)") for profit in profits]

        numTests = profits.count()
        ind = matplotlib.numpy.arange(numTests) # the x locations for the groups
        # Set color transparency (0: transparent; 1: solid)
        bar_width = 0.35
        opacity = 0.4
        # Remove plot frame
        #ax.set_frame_on(False)
        #plt.subplots_adjust(bottom=0.6,hspace = 0.2)
        #ax.title.set_position((0.1,1.08))#(x,y) x chay tu trái sang phải 0.1->1.1 , y chay tu dưới lên trên: 0.1->1.1

        ax.plot(ind, profs,color='r', label='Price Upt')
        ax.scatter(ind, profs,color='r')

        ax.plot(ind, prof_upts,color='g', label='Price Upt')
        ax.scatter(ind, prof_upts,color='g')

        ax.plot(ind, prof_acts, color='black', label='Revenue Upt')
        ax.scatter(ind, prof_acts, color='black')

        ax.set_xlabel('Time')
        ax.set_ylabel('($)')
        ax.set_title('Revenue, Expense by Date.')

        #updates_n = matplotlib.dates.date2num(updates)
        ax.set_xticks(ind + bar_width/2)
        ax.set_xticklabels(updates, rotation=90, size=10)
        ax.legend()
        #ax.grid(True)
        autolabel_dot_billion(ind, profs, 1., ax, 'r', 'bottom')#10^11
        autolabel_dot_billion(ind, prof_upts, 1., ax, 'g', 'bottom')#10^11
        autolabel_dot_billion(ind, prof_acts , 1., ax, 'black', 'bottom')#10^11

        fig.autofmt_xdate()
        canvas = FigureCanvas(fig)
        response = HttpResponse(content_type='image/png')
        canvas.print_png(response)
        return response


class weather_chart_view(TemplateResponseMixin, View):#LoginRequiredMixin,DetailView):
    template_name = 'menu/django_chartit.html'
    print('start chart')
    def get(self,request):
        #if request.user.username == 'lanpq':
        if request.user.is_authenticated():
        #def weather_chart_view(request):
            #Step 1: Create a DataPool with the data we want to retrieve.
            print(request.user)
            from menu.models import MonthlyWeatherByCity
            cht = get_chartit(MonthlyWeatherByCity)
            sites=Sites.objects.all()
            tasks=Tasklist.objects.all()
            #Step 3: Send the chart object to the template.
            return self.render_to_response({'weatherchart': cht, 'sites': sites, 'tasks': tasks})
        #else:
        return HttpResponseForbidden("Restricted Access")
        #return self.render_to_response({'weatherchart': cht})

def get_chartit(MonthlyWeatherByCity):
    from chartit import DataPool
    weatherdata = \
        DataPool(
           series=
            [{'options': {
               'source': MonthlyWeatherByCity.objects.all()},
              'terms': [
                'month',
                'houston_temp',
                'boston_temp']}
             ])

    #Step 2: Create the Chart object
    from chartit import Chart
    cht = Chart(
            datasource = weatherdata,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'boston_temp',
                    'houston_temp']
                  }}],
            chart_options =
              {'title': {
                   'text': 'Weather Data of Boston and Houston'},
               'xAxis': {
                    'title': {
                       'text': 'Month number'}}})
    return cht


class budget_chart_view(TemplateResponseMixin, View):#LoginRequiredMixin,DetailView):#TemplateResponseMixin, View
    template_name = 'menu/itemcontent/reports/budgets/django_chartit.html'
    print('start chart')
    def get(self,request):
        #if request.user.username == 'lanpq':
        if request.user.is_authenticated():
        #def weather_chart_view(request):
            #Step 1: Create a DataPool with the data we want to retrieve.
            print(request.user)
            #from menu.models import MonthlyWeatherByCity
            #cht = get_chartit(MonthlyWeatherByCity)
            b = Budgets.objects.values_list('budgetid','price','priceupt','update','sitename').raw(
                '''
                SELECT budgets."BudgetID", budgets."Update",budgets."Price",budgets."PriceUpt", maxdatebudgets."SiteID"
                FROM budgets,
                (select "TaskID",max("Update") as "maxUpdate","SiteName",
                  (select sites."SiteID" from sites where sites."SiteName"=budgets."SiteName") "SiteID"
                from budgets
                group by "TaskID","SiteName"
                order by "TaskID","SiteName") as maxdatebudgets
                where budgets."TaskID"=maxdatebudgets."TaskID" and budgets."SiteName"=maxdatebudgets."SiteName"
                and budgets."Update"=maxdatebudgets."maxUpdate"  and char_length(budgets."TaskID") <= 4 and budgets."SiteName"='118_Casino-PQ'
                order by budgets."SiteName"
                '''
            )
            #cht=get_budget_chartit(b)
            sites=Sites.objects.all()
            tasks=Tasklist.objects.all()
            #Step 3: Send the chart object to the template.
            return self.render_to_response({'budgets': b, 'sites': sites, 'tasks': tasks})
        #else:
        return HttpResponseForbidden("Restricted Access")
        #return self.render_to_response({'weatherchart': cht})

'''
demo weather data
'''
def get_budget_chartit(modelname):
    from chartit import DataPool
    #from datetime import time
    #from datetime import datetime, time
    import time
    weatherdata = \
        DataPool(
           series=
            [{'options': {
               'source': modelname},
              'terms': [
                  ('update', lambda d: time.mktime(d.timetuple())),
                'price']}
             ])

    #Step 2: Create the Chart object
    from chartit import Chart
    cht = Chart(
            datasource = weatherdata,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'update': [
                    'price']
                  }}],
            chart_options =
              {'title': {
                   'text': 'Data chart'},
               'xAxis': {
                    'title': {
                       'text': 'Date'}}},
            x_sortf_mapf_mts=(None, lambda i: datetime.fromtimestamp(i).strftime("%D:%M"), False)
            ),
    return cht

'''profit demo
        site=get_object_or_404(Sites, siteid=site_id)
        print('plot %s' % site.sitename)
        profits = Profits.objects.filter(sitename=site.sitename)

        profs = [profit.profit for profit in profits]
        prof_upts = [profit.profitupt for profit in profits]
        prof_acts = [profit.profitact for profit in profits]
        updates = [profit.update.strftime("%Y-%m-%d(%Hh)") for profit in profits]

        numTests = profits.count()
        ind = matplotlib.numpy.arange(numTests) # the x locations for the groups
'''
class profit_chart_view(TemplateResponseMixin, View):#LoginRequiredMixin,DetailView):#TemplateResponseMixin, View
    template_name = 'menu/itemcontent/reports/budgets/profit_chartit.html'
    print('start chart')
    def get(self,request, site_id=None):
        #if request.user.username == 'lanpq':
        if request.user.is_authenticated():
        #def weather_chart_view(request):
            #Step 1: Create a DataPool with the data we want to retrieve.
            print(request.user)
            #from menu.models import MonthlyWeatherByCity
            #cht = get_chartit(MonthlyWeatherByCity)
            if site_id:
                site=get_object_or_404(Sites, siteid=site_id)
                print('plot %s' % site.sitename)
                profits = Profits.objects.filter(sitename=site.sitename)

            profs = [profit.profit for profit in profits]
            prof_upts = [profit.profitupt for profit in profits]
            prof_acts = [profit.profitact for profit in profits]
            updates = [profit.update.strftime("%Y-%m-%d(%Hh)") for profit in profits]

            numTests = profits.count()
            ind = matplotlib.numpy.arange(numTests)
            sites=Sites.objects.all()
            tasks=Tasklist.objects.all()
            #Step 3: Send the chart object to the template.
            return self.render_to_response({'ind': ind,'profs':profs,'prof_upts':prof_upts,'prof_acts':prof_acts,
                                            'updates':updates,'sites': sites, 'tasks': tasks})
        #else:
        return HttpResponseForbidden("Restricted Access")