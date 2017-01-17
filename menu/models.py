import datetime
import os
from time import strptime

import decimal
import matplotlib
import numpy as np
import simplejson as simplejson
import timestring as timestring
from django.contrib.auth.models import User, Group
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.files.storage import FileSystemStorage

from django.core.serializers.json import DjangoJSONEncoder
from django.core.urlresolvers import reverse
from django.db import models, connection
# Create your models here.
from django.db.models import Max
from django.forms import Textarea
from django.template.loader import render_to_string
from django.utils.functional import lazy

from analytics import settings
from biapp.models import DataType, ChartType, ColumnList, ReportList

from budgets.models import * #Sites, Profits, Budgets, Revenues, Tasklist
from menu import plot
from menu.fields import OrderField
from menu.funcs import pd_strftime, pd_tojson_withfilter, my_custom_sql, pd_tojson_bycols, pd_tojson_byrows
from menu.maths import find_lineAB
from postage.models import * #RegisteredVehicle, VehicleInOut, VehicleSupplier, CardType, VehicleType


class MenuFunction(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    orderview = models.PositiveIntegerField()

    class Meta:
        ordering = ('orderview','name')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('menu:menufunction_dashboard_by_category', args=[self.slug])


#danh muc menu theo chức năng
class MenuHeader(models.Model):
    owner = models.ForeignKey(User, related_name='rel_menu_headers_users')
    menufunction = models.ForeignKey(MenuFunction, related_name='rel_menu_headers_functions')
    employees = models.ManyToManyField(User, related_name='rel_menuheaders_employees', blank=True)
    name= models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    image = models.ImageField(upload_to='image/menuheader/%Y/%m/%d', blank=True)
    #bosung them
    description = models.TextField(blank=True)
    orderview = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    createddate = models.DateTimeField(auto_now_add=True)
    updateddate = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'menu header'
        verbose_name_plural = 'menu headers'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('menu:menuheader_list', args=[self.id, self.slug])


class MenuDetail(models.Model):
    menuheader = models.ForeignKey(MenuHeader, related_name='rel_menu_details')
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='image/menudetail/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    #price = models.DecimalField(max_digits=10, decimal_places=2)
    #stock = models.PositiveIntegerField()
    #orderview = models.PositiveIntegerField()
    orderview = OrderField(blank=True, for_fields=['menuheader'])
    available = models.BooleanField(default=True)
    createddate = models.DateTimeField(auto_now_add=True)
    updateddate = models.DateTimeField(auto_now=True)

    class Meta:
        #ordering = ('name',)
        ordering = ['orderview']
        index_together = (('id', 'slug'),)

    def __str__(self):
        #return self.name
        return '{}. {}'.format(self.orderview, self.name)

    def get_absolute_url(self):
        return reverse('menu:menudetail_list', args=[self.id, self.slug])


class MenuDetailEmployees(models.Model):
    menudetail = models.ForeignKey(MenuDetail, related_name='rel_mdes_mds')
    employee = models.ForeignKey(User, related_name='rel_mdes_users')
    #description = models.TextField(max_length=10,blank=True)#
    description = models.CharField(max_length=200, db_index=True)
    available = models.BooleanField(default=True)
    createddate = models.DateTimeField(auto_now_add=True)
    updateddate = models.DateTimeField(auto_now=True)


class MonthlyWeatherByCity(models.Model):
    month = models.IntegerField()
    boston_temp = models.DecimalField(max_digits=5, decimal_places=1)
    houston_temp = models.DecimalField(max_digits=5, decimal_places=1)


class ItemContent(models.Model):
    menudetail = models.ForeignKey(MenuDetail, related_name='rel_itemcontents_menudetails')
    itemtype = models.ForeignKey(ContentType, limit_choices_to={'model__in':('text','video','image','file','chart','profit_table','url')})
    objid = models.PositiveIntegerField()
    item = GenericForeignKey('itemtype', 'objid')
    orderview = OrderField(blank=True, for_fields=['menudetail'])

    class Meta:
        ordering = ['orderview']

size_list = (
    ('2', 'Size 2/12'),
    ('3', 'Size 3/12'),
    ('4', 'Size 4/12'),
    ('5', 'Size 5/12'),
    ('6', 'Size 6/12'),
    ('7', 'Size 7/12'),
    ('8', 'Size 8/12'),
    ('9', 'Size 9/12'),
    ('10', 'Size 10/12'),
    ('11', 'Size 11/12'),
    ('12', 'Size 12/12'),
)


##test permission file in media dir
private_media = FileSystemStorage(location=settings.PRIVATE_MEDIA_ROOT,
                                  base_url=settings.PRIVATE_MEDIA_URL,)

##########owner title createddate updateddate haveTitle haveLink size
class ItemBase(models.Model):
    owner = models.ForeignKey(User, related_name='%(class)s_related')
    title = models.CharField(max_length=250)
    createddate = models.DateTimeField(auto_now_add=True)
    updateddate = models.DateTimeField(auto_now=True)
    haveTitle = models.BooleanField(default=True)
    haveLink = models.BooleanField(default=False)
    size = models.CharField(max_length=2,blank=True, choices = size_list,default='6')

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

    def render(self):
        #dang test truyen site vào render-> type content *.html
        #test ok
        #psite = Sites.objects.all()
        return render_to_string('menu/itemcontent/{}.html'.format(self._meta.model_name), {'item': self})

class Text(ItemBase):
    content = models.TextField()

class File(ItemBase):
    file = models.FileField(upload_to='files')

class Image(ItemBase):
    file = models.FileField(upload_to='protected') #'images')
    #protected_url = models.URLField(blank=True)
    photo = models.ImageField(storage=private_media)
    '''
    def render(self):
        #dang test truyen site vào render-> type content *.html
        #test ok
        #psite = Sites.objects.all()
        #protected = reverse('upload_file_serve', args=[os.path.basename(self.file.file.name)])
        print('render')
        #print(protected)
        return render_to_string('menu/itemcontent/{}.html'.format(self._meta.model_name), {'item': self}) #,'protected':protected})
    '''

class Video(ItemBase):
    url = models.URLField()

class Url(ItemBase):
    url = models.CharField(max_length=250)
    icon = models.FileField(upload_to='icons')

MY_CHOICES = (
    ('a1', 'Option 11'),
    ('a2', 'Option 22'),
    ('a3', 'Option 32'),
)

############################################################################
##se hoan thanh sau: muc tieu - chon field tự động, thiet kế cho report động
def get_menu_choices(datatype):
    choices_tuple = []
    #if datatype == 'sitestable':
    ##############test ok###############
    #choices_tuple = [(field,field) for field in Sites._meta.get_all_field_names()]
    #choices_tuple2=tuple((choices_tuple, choices_tuple))
    #print(choices_tuple)
    ######################################
    if datatype == 'sitestable':
        choices_tuple = [(field,field) for field in Sites._meta.get_all_field_names()]
    elif datatype == 'budgetstable':
        choices_tuple = [(field,field) for field in Budgets._meta.get_all_field_names()]
    elif datatype == 'profitstable':
        choices_tuple = [(field,field) for field in Profits._meta.get_all_field_names()]

    #choices_tuple = (
    #    ('b1', 'Option b1'),
    #    ('b2', 'Option b2'),
    #    ('b3', 'Option b3'),
    #)
    print(datatype)
    print(choices_tuple)
    #do your stuff
    return choices_tuple

############################################################################
##se hoan thanh sau: muc tieu - chon field tự động, thiet kế cho report động
#class Chart_bk(ItemBase):
#    file = models.FileField(upload_to='charts')
#    charttype = models.ForeignKey(ChartType, related_name='rel_charts_charttypes')
#    datatype = models.ForeignKey(DataType, related_name='rel_charts_datatypes')
#    content = models.TextField()
#    choices_f = models.CharField(max_length=50, blank=True)#, choices = MY_CHOICES)

#    #def __init__(self,  *args, **kwargs):
#    #    super(Chart, self).__init__(*args, **kwargs)
#    #    #choices_tuple = ['z1','z2','z3','z4','z5']
#    #    #self._meta.get_field_by_name('choices_f')[0]._choices = MY_CHOICES #lazy(get_menu_choices, list)()#choices_tuple# get_menu_choices()
#    #    self._meta.get_field_by_name('choices_f')[0]._choices = get_menu_choices(self.datatype.slug)
#    #    #self.fields['choices_f'] = forms.ChoiceField(choices = MY_CHOICES)

table_list=(('Sites','Sites'), ('Profits','Profits'), ('Budgets','Budgets'), ('Revenues','Revenues'), ('Tasklist','Tasklist'),
             ('RegisteredVehicle','RegisteredVehicle'), ('VehicleInOut','VehicleInOut'), ('VehicleSupplier','VehicleSupplier'),
             ('CardType','CardType'), ('VehicleType','VehicleType'),)
table_list2=('sites', 'profits', 'budgets', 'revenues','tasklist') #viết hoa 'Sites' khi getmodel nó k hieu, phải viết thường 'sites'
             #,'registeredvehicle')#,'VehicleInOut','VehicleSupplier','CardType','VehicleType')

def get_col_list(table_list2):
    from django.apps import apps
    choices_tuple = []
    for t in table_list2:
        m=apps.get_model(app_label='budgets', model_name=t)
        choices_tuple += [(field,field) for field in m._meta.get_all_field_names()]
    print(choices_tuple)
    from django.db.models.loading import get_models
    for model in get_models():
        # Do something with your model here
        print(model.__name__, [x.name for x in model._meta.fields])
    return choices_tuple

#file charttype datatype columnlist content
# axis_x1 axis_x2 axis_x3 axis_x4 axis_x5 axis_y1 axis_y2 axis_y3 axis_y4 axis_y5
from smart_selects.db_fields import ChainedForeignKey
class Chart(ItemBase):
    file = models.FileField(upload_to='charts',blank=True)
    content = models.TextField()
    #cho phep chon cách tao itemcontent chart theo 2 cách: từ danhsach report hoặc từ DataType
    #viewreportby=models.PositiveIntegerField(blank=True, choices=((1,'Chart by Report List'),(2,'Chart by Data')))
    viewreportby=models.PositiveIntegerField(default=1, blank=True, choices=((1,'Chart by Report List'),(2,'Chart by Data')))
    charttype = models.ForeignKey(ChartType, related_name='rel_charts_charttypes')
    datatype = models.ForeignKey(DataType, related_name='rel_charts_datatypes', default='budgets')

    #columnlist = ChainedForeignKey(ColumnList, chained_field='datatype',
    #                            chained_model_field='datatype', show_all=False, auto_choose=True )
    #columnlist = models.ForeignKey(ColumnList, related_name='rel_charts_columnlists',default=1)

    reportlist = models.ForeignKey(ReportList, related_name='rel_charts_reportlists')
    sqlstring=models.TextField(blank=True)
    sqlextra=models.TextField(blank=True)
    sqlfilter=models.TextField(blank=True)
    hierarchy = models.CharField(max_length=3, blank=True, choices=(('yes','Yes'),('no','No')))
    axis_x1 = models.CharField(max_length=20,blank=True)
    axis_x2 = models.CharField(max_length=20,blank=True)#models.ForeignKey(ColumnList, related_name='rel_charts_axis_x2',blank=True)
    axis_x3 = models.CharField(max_length=20,blank=True)
    axis_x4 = models.CharField(max_length=20,blank=True)
    axis_x5 = models.CharField(max_length=20,blank=True)
    axis_y1 = models.CharField(max_length=20,blank=True)
    axis_y2 = models.CharField(max_length=20,blank=True)
    axis_y3 = models.CharField(max_length=20,blank=True)
    axis_y4 = models.CharField(max_length=20,blank=True)
    axis_y5 = models.CharField(max_length=20,blank=True)

    '''20161222
    chay ok:colname lấy được danh sách từ table_list2, nhưng chỉ lấy lúc khởi tạo,
    vấn đề là muốn khi tablename thay doi thì colname cũng phải thay đổi theo.
    tablename = models.CharField(max_length=50, blank=True, choices=table_list)
    colname = models.CharField(max_length=50, blank=True)
    def __init__(self,  *args, **kwargs):
        super(Chart, self).__init__(*args, **kwargs)
        self._meta.get_field_by_name('colname')[0]._choices = get_col_list(table_list2)
        #from django import forms
        #self.fields['colname'] = forms.ChoiceField(choices = get_col_list(table_list2))
    '''
    '''
        from datetime import date, timedelta as td
        d1 = date(2008, 8, 15)
        d2 = date(2008, 9, 15)
        delta = d2 - d1
        for i in range(delta.days + 1):
        print d1 + td(days=i)
        '''

    def render(self):
        #dang test truyen site vào render-> type content *.html
        #test ok
        print('model: tao renderlink')
        if self._meta.model_name=='chart':
            renderlink = 'menu/itemcontent/reports/{}_{}.html'.format(self.datatype.slug, self.charttype.slug)
            if self.reportlist_id == 'rep2':
                renderlink = 'menu/itemcontent/reports/list/{}_{}.html'.format(self.reportlist.id, self.reportlist.slug)
                sites = Sites.objects.all()
                budgets = Budgets.objects.raw(self.sqlstring)
                return render_to_string(renderlink, {'item': self, 'sites': sites, 'budgets':budgets})
            if self.reportlist_id == 'rep3':
                renderlink = 'menu/itemcontent/reports/list/{}_{}.html'.format(self.reportlist.id, self.reportlist.slug)
                sites = Sites.objects.all()
                budgets = Budgets.objects.raw(self.sqlstring)
                return render_to_string(renderlink, {'item': self, 'sites': sites, 'budgets':budgets})
            if self.reportlist_id == 'rep4':
                renderlink = 'menu/itemcontent/reports/list/{}_{}.html'.format(self.reportlist.id, self.reportlist.slug)
                sites = Sites.objects.all()
                budgets = list(my_custom_sql(self.sqlstring))
                print(sites)
                print(self.sqlstring)
                print(budgets)
                return render_to_string(renderlink, {'item': self, 'sites': sites, 'budgets':budgets})
            if self.reportlist_id == 'rep5':
                renderlink = 'menu/itemcontent/reports/list/{}_{}.html'.format(self.reportlist.id, self.reportlist.slug)
                sites = Sites.objects.all()
                datas = list(my_custom_sql(self.sqlstring))
                print(sites)
                print(self.sqlstring)
                print(datas)
                list_y1 = [d[self.axis_y1] for d in datas]
                list_y2 = [d[self.axis_y2] for d in datas]
                list_y3 = [d[self.axis_y3] for d in datas]
                list_x1 = [d[self.axis_x1].strftime("%Y-%m-%d(%Hh)") for d in datas]
                list_x1time = [d[self.axis_x1] for d in datas]
                numTests = len(datas)#.count()
                ind = matplotlib.numpy.arange(numTests)

                '''
                Vẽ thêm đường thẳng nối từ điểm Actual hiện tại đến Plan/Update cuối dự án
                '''
                from dateutil.rrule import rrule, MONTHLY

                from datetime import date
                import time

                ##import datetime as DT
                # until=DT.date.today()
                #dataextras = list(my_custom_sql(self.sqlextra))#select ..xi,yi, xj, yj
                dataextras = list(my_custom_sql('''
                    select "SiteID","End", max("Update") from revenues where "SiteID"='S123' GROUP BY "SiteID","End"
                    '''))
                print(dataextras)
                import timestring
                #x1i = datetime.datetime.strptime(list_x1[-1],"%Y-%m-%d(%Hh)")
                x_start = list_x1time[-1]
                x_end = [dataextra["End"] for dataextra in dataextras][0]
                print('start: %s , end: %s' %(x_start,x_end))
                print(x_start)
                print(x_end)
                #months = [dt.strftime("%m") for dt in rrule(MONTHLY, dtstart=date(2016, 9, 15), until=date(2017, 1, 5))]
                months = [dt.strftime("%m") for dt in rrule(MONTHLY, dtstart=x_start, until=x_end )]
                print(months)
                countextra=len(months)
                y1_extra = [list_y1[-1]]*countextra
                y2_extra = [list_y2[-1]]*countextra
                print('y1: %s' %list_y1[-1])
                print('y2: %s' %list_y2[-1])
                y3_extra = find_lineAB(x_start.month, list_y3[-1], x_start.month+countextra,list_y1[-1],months)
                list_y1 = list_y1 + y1_extra
                list_y2 = list_y2 + y2_extra
                list_y3 = list_y3 + y3_extra
                list_x1 = list_x1 + months
                return render_to_string(renderlink, {'item': self, 'sites': sites,
                                                     'ind': ind,'list_y1':list_y1,'list_y2':list_y2,'list_y3':list_y3,
                                            'list_x1':list_x1})
            if self.reportlist_id == 'rep6':
                renderlink = 'menu/itemcontent/reports/list/{}_{}.html'.format(self.reportlist.id, self.reportlist.slug)
                print('############# report số:  %s' %self.reportlist_id)
                import pandas as pd
                #sites = pd.DataFrame(my_custom_sql('''select * from sites'''))
                test=list(my_custom_sql(self.sqlfilter))
                #print(test)
                pdFilter = pd.DataFrame(my_custom_sql(self.sqlfilter))
                filterColumnList=[col for col in pdFilter.columns]
                filterColumnList=[filterColumnList[0]]#chỉ lấy cột đầu và append thêm Update
                filterColumnList.append('Update')#kết quả ['SiteID', 'SiteName']
                print(filterColumnList)
                pdData = pd.DataFrame(my_custom_sql(self.sqlstring))
                print(self.sqlstring)
                '''
                ############ STEP 1 ############'''
                #SiteID | Update | Label | End | Revenue | RevenueUpt |RevenueAct|
                #chuẩn hóa dữ liệu trước khi lên chart,
                #chuyen sang kieu float trước khi gán ='' vì '' k thể convert to float
                pdData['Label'] = pdData[self.axis_x1].apply(pd_strftime)
                pdData[self.axis_y1] = pdData[self.axis_y1].astype('float64')
                pdData[self.axis_y2] = pdData[self.axis_y2].astype('float64')
                pdData[self.axis_y3] = pdData[self.axis_y3].astype('float64')
                pdData['Extra'] = ''

                '''
                Vẽ thêm đường thẳng nối từ điểm Actual hiện tại đến Plan/Update cuối dự án
                du lieu đầu vào:
                '''
                from dateutil.rrule import rrule, MONTHLY
                '''
                ############ STEP 2 ############'''
                #láy giá trị ngày cuối cùng của pdData làm ngày đầu của pdDataExtra
                # muốn vậy cần phải group theo ngày Update, sau đó lấy last()
                pdStartValue=pdData.groupby(filterColumnList).last().reset_index()
                pdStartValue = pdStartValue.groupby(filterColumnList[0]).last().reset_index()
                pdStartValue['StartValueAct']=pdStartValue[self.axis_y3]
                #pdDataExtras = list(self.my_custom_sql(self.sqlextra))#select ..xi,yi, xj, yj
                #pdDataExtras = pd.DataFrame(self.my_custom_sql('''select "SiteID","End", "Update" from revenues'''))
                pdEndValue = pd.DataFrame(my_custom_sql(self.sqlextra))
                #neu cau sql k có group MAX thì dùng lenh duoi, nếu co group MAX thì k cần dùng
                pdEndValue=pdEndValue.groupby(filterColumnList).last().reset_index()
                pdEndValue = pdEndValue.groupby(filterColumnList[0]).last().reset_index()
                #lấy pd voi 2 column Site & End date của dự án, rộng ra là End của DataExtra(dulieu bất kỳ)
                #sau đó merge theo chiều ngang, nối End vào cuối bên phải datatemp
                pdEndValue=pdEndValue[[filterColumnList[0],'End']]
                pdDataExtras=pd.merge(pdStartValue, pdEndValue, on=[filterColumnList[0]])

                '''
                ############ STEP 3 ############
                #khoi tao gia tri Line Extra, y=ax+b với A(x1,y1), B(x2,y2) cho trước
                #A là Update cuối của pdData, B là End Data của DataExtra
                '''
                print("start1")
                pdExtraByRow = pd.DataFrame()
                for i,d2 in pdDataExtras.iterrows():
                    #print(d2["SiteID"])
                    months = [dt.strftime("%m") for dt in rrule(MONTHLY, dtstart=d2["Update"], until=d2["End"] )]
                    countextra=len(months)
                    pdExtraByRow[filterColumnList[0]]=[d2[filterColumnList[0]]]*countextra
                    pdExtraByRow["Label"] = pd.DataFrame(months)
                    pdExtraByRow[self.axis_y1] = [d2[self.axis_y1]]*countextra
                    pdExtraByRow[self.axis_y2] = [d2[self.axis_y2]]*countextra
                    pdExtraByRow[self.axis_y3] = ''
                    extra = find_lineAB(d2["Update"].month, d2["StartValueAct"], d2["Update"].month+countextra,d2[self.axis_y1],months)
                    pdExtraByRow["Extra"]=pd.DataFrame(extra)
                    pdDataExtras = pdDataExtras.append(pdExtraByRow)
                '''
                ############ STEP 4 ############'''
                pdData = pdData.append(pdDataExtras).reset_index()
                #convert pandas to json, có chèn thêm tên filter:là giá trị để javascript có thể filter
                #vidu o day là 'site': 'S103'
                json_data=pd_tojson_withfilter(pdData, pdFilter, filterColumnList[0])
                json_filter=pd_tojson_byrows(pdFilter)
                #print(json_filter)
                return render_to_string(renderlink, {'item': self, 'json_filter': json_filter, 'json_data':json_data})

        else:
            renderlink = 'menu/itemcontent/{}.html'.format(self._meta.model_name)

        if self.datatype.slug == 'sitestable':
            print('profits: siteid %s' %{self.datatype.slug})
            sites = Sites.objects.all()
            return render_to_string(renderlink, {'item': self, 'sites': sites})#, 'tables':tables
        elif self.datatype.slug == 'budgetstable':
            print('budgets: siteid %s' %{self.datatype.slug})
            sites = Sites.objects.all()
            #budgets = Budgets.objects.all()
            #lay budget của ngày mới nhất

            self.sqlstring='''
                SELECT budgets.*, maxdatebudgets."SiteID",
                (case when budgets."TaskID"='A' then concat(maxdatebudgets."SiteID",'0A')
                else concat(maxdatebudgets."SiteID",replace(budgets."TaskID",'.','_'))
                 end) "TaskKey",

                (CASE WHEN budgets."TaskID"<>'A' THEN
                    (case  when position('.' in budgets."TaskID")>0 then
                        concat(maxdatebudgets."SiteID",replace(substring(budgets."TaskID", 1, length(budgets."TaskID")-position('.' in (reverse(budgets."TaskID")))),'.','_'))
                        else concat(maxdatebudgets."SiteID",'0A')
                    end
                    )
                    when budgets."TaskID"='A' then maxdatebudgets."SiteID"
                END) "TaskKeyParent"
                FROM budgets,
                (select "TaskID",max("Update") as "maxUpdate","SiteName",
                (select sites."SiteID" from sites where sites."SiteName"=budgets."SiteName") "SiteID"
                from budgets
                group by "TaskID","SiteName"
                order by "TaskID","SiteName") as maxdatebudgets
                where budgets."TaskID"=maxdatebudgets."TaskID" and budgets."SiteName"=maxdatebudgets."SiteName"
                and budgets."Update"=maxdatebudgets."maxUpdate"  and char_length(budgets."TaskID") <= 4
                order by budgets."SiteName", "TaskKey"
                '''

            budgets = Budgets.objects.raw(self.sqlstring)
            return render_to_string(renderlink, {'item': self, 'sites': sites, 'budgets':budgets})
        elif self.datatype.slug == 'profitstable':
            print('profits: siteid %s' %{self.datatype.slug})
            sites = Sites.objects.all()
            profits = Profits.objects.all()
            return render_to_string(renderlink, {'item': self, 'sites': sites, 'profits':profits})
        elif self.datatype.slug == 'revenuestable':
            sites = Sites.objects.all()
            revenues = Revenues.objects.all()
            return render_to_string(renderlink, {'item': self, 'sites': sites, 'revenues':revenues})
        elif self.datatype.slug == 'registeredvehicle':
            registeredvehicles = RegisteredVehicle.objects.all()
            return render_to_string(renderlink, {'item': self, 'registeredvehicles':registeredvehicles})
        elif self.datatype.slug == 'vehicleinout':
            vehicleinouts = VehicleInOut.objects.all()
            return render_to_string(renderlink, {'item': self, 'vehicleinouts':vehicleinouts})
        elif self.datatype.slug == 'vehiclesupplier':
            vehiclesuppliers = VehicleSupplier.objects.all()
            return render_to_string(renderlink, {'item': self, 'vehiclesuppliers':vehiclesuppliers})
        elif self.datatype.slug == 'vehicletype':
            vehicletypes = VehicleType.objects.all()
            return render_to_string(renderlink, {'item': self, 'vehicletypes':vehicletypes})
        elif self.datatype.slug == 'cardtype':
            cardtypes = CardType.objects.all()
            return render_to_string(renderlink, {'item': self, 'cardtypes':cardtypes})
        elif self.datatype.slug == 'tasklist':
            tasklists = Tasklist
            return render_to_string(renderlink, {'item': self, 'tasklists':tasklists})
        elif self.datatype.slug == 'chartit':
            cht = plot.get_chartit(MonthlyWeatherByCity)
            #Step 3: Send the chart object to the template.
            return render_to_string(renderlink, {'item': self, 'weatherchart': cht})


class Profit_Table(ItemBase):
    content = models.TextField()

    def render(self):
        #dang test truyen site vào render-> type content *.html
        #test ok
        print('model: render table')


        sites = Sites.objects.all()

        budgets = Budgets.objects.raw(
            '''
            SELECT budgets.*, maxdatebudgets."SiteID",

		    (case when budgets."TaskID"='0A' then concat(maxdatebudgets."SiteID",'0A')
		    else concat(maxdatebudgets."SiteID",replace(budgets."TaskID",'.','_'))
		     end) "TaskKey",

            (CASE WHEN budgets."TaskID"<>'0A' THEN
                (case  when position('.' in budgets."TaskID")>0 then
                    concat(maxdatebudgets."SiteID",replace(substring(budgets."TaskID", 1, length(budgets."TaskID")-position('.' in (reverse(budgets."TaskID")))),'.','_'))
                    else concat(maxdatebudgets."SiteID",'0A')
                end
                )
	    	    when budgets."TaskID"='0A' then maxdatebudgets."SiteID"
    		END) "TaskKeyParent"
            FROM budgets,
            (select "TaskID", max("Update") as "maxUpdate", "SiteID",
            (select sites."SiteName" from sites where sites."SiteID"=budgets."SiteID") "SiteName"
            from budgets
            group by "TaskID","SiteID"
            order by "TaskID","SiteID") as maxdatebudgets
            where budgets."TaskID"=maxdatebudgets."TaskID" and budgets."SiteID"=maxdatebudgets."SiteID"
            and budgets."Update"=maxdatebudgets."maxUpdate"  and char_length(budgets."TaskID") <= 4
            order by budgets."SiteID", "TaskKey"
            '''
        )
        ######chay duoc nhung qua chậm
        #arraytasks=[]
        #for k in range(len(list(budgets))):
        #    arraytasks.append({'sitename':budgets[k].sitename,'taskid':budgets[k].taskid})

        #arraytasks = [{'sitename':budgets[k].sitename,'taskid':budgets[k].taskid} for k in range(len(list(budgets))) ]

        #budgets = Budgets.objects.all()
        return render_to_string('menu/itemcontent/{}.html'.format(self._meta.model_name),
                                {'item': self, 'sites': sites, 'budgets':budgets})