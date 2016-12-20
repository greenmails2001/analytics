import os

from django.contrib.auth.models import User, Group
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.files.storage import FileSystemStorage
from django.core.urlresolvers import reverse
from django.db import models
# Create your models here.
from django.db.models import Max
from django.forms import Textarea
from django.template.loader import render_to_string
from django.utils.functional import lazy

from analytics import settings
from budgets.models import Sites, Profits, Budgets, Revenues, Tasklist
from menu import plot
from menu.fields import OrderField
from postage.models import RegisteredVehicle, VehicleInOut, VehicleSupplier, CardType, VehicleType


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


class DataType(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, db_index=True)
    image = models.ImageField(upload_to='image/datatype/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        #return self.name
        return '{}- {}'.format(self.id, self.name)

    def get_absolute_url(self):
        return reverse('menu:datatype_list', args=[self.id, self.slug])


class ChartType(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    #datatype = models.ForeignKey(DataType, related_name='rel_charttypes_datatypes')
    image = models.ImageField(upload_to='image/charttype/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        #return self.name
        return '{}. {}'.format(self.id, self.name)

    def get_absolute_url(self):
        return reverse('menu:charttype_list', args=[self.id, self.slug])


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

##########
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


class Chart(ItemBase):
    file = models.FileField(upload_to='charts')
    charttype = models.ForeignKey(ChartType, related_name='rel_charts_charttypes')
    datatype = models.ForeignKey(DataType, related_name='rel_charts_datatypes')
    content = models.TextField()

    def render(self):
        #dang test truyen site vào render-> type content *.html
        #test ok
        print('model: tao renderlink')
        if self._meta.model_name=='chart':
            renderlink = 'menu/itemcontent/reports/{}_{}.html'.format(self.datatype.slug, self.charttype.slug)
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
            budgets = Budgets.objects.raw(
                '''
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
            )
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
        )
        ######chay duoc nhung qua chậm
        #arraytasks=[]
        #for k in range(len(list(budgets))):
        #    arraytasks.append({'sitename':budgets[k].sitename,'taskid':budgets[k].taskid})

        #arraytasks = [{'sitename':budgets[k].sitename,'taskid':budgets[k].taskid} for k in range(len(list(budgets))) ]



        #budgets=Budgets.objects.all().aggregate(Max('update'))

        #budgets = Budgets.objects.values('taskid','sitename','update').filter(taskid__in=(
        #    Budgets.objects
        #        .values('taskid','sitename')
        #        .annotate(Max('update'))
        #        .values_list('taskid', flat=True)
        #))

        #budgets=Budgets.objects.annotate(maxdate=Max('update')).order_by('taskid','sitename').values_list('taskid','sitename')
        #budgets = Budgets.objects.filter(
        #    budgetsmax.filter(taskid__isnull=False)).filter(
         #   budgetsmax.filter(sitename__isnull=False)).distinct().values_list('taskid','sitename','update')

        #budgetsz=Budgets.objects.annotate(maxdate=Max('update')).order_by('taskid','sitename').\
        #    values_list('taskid','sitename','maxdate').\
        #    filter(budgets__taskid__isnull=False).\
        #    filter(budgets__sitename__isnull=False)


        #budgets = Budgets.objects.all()
        return render_to_string('menu/itemcontent/{}.html'.format(self._meta.model_name),
                                {'item': self, 'sites': sites, 'budgets':budgets})