from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.db import models
# Create your models here.
from django.db.models import Max
from django.template.loader import render_to_string

from budgets.models import Sites, Profits, Budgets
from menu.fields import OrderField


class MenuFunction(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)

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


class ChartType(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='image/charttype/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        #return self.name
        return '{}. {}'.format(self.name, self.description)

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


class ItemContent(models.Model):
    menudetail = models.ForeignKey(MenuDetail, related_name='rel_itemcontents_menudetails')
    itemtype = models.ForeignKey(ContentType, limit_choices_to={'model__in':('text','video','image','file','chart','profit_table','url')})
    objid = models.PositiveIntegerField()
    item = GenericForeignKey('itemtype', 'objid')
    orderview = OrderField(blank=True, for_fields=['menudetail'])

    class Meta:
        ordering = ['orderview']


##########
class ItemBase(models.Model):
    owner = models.ForeignKey(User, related_name='%(class)s_related')
    title = models.CharField(max_length=250)
    createddate = models.DateTimeField(auto_now_add=True)
    updateddate = models.DateTimeField(auto_now=True)

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
    file = models.FileField(upload_to='images')

class Video(ItemBase):
    url = models.URLField()

class Url(ItemBase):
    url = models.CharField(max_length=250)
    icon = models.FileField(upload_to='icons')

class Chart(ItemBase):
    file = models.FileField(upload_to='charts')
    charttype = models.ForeignKey(ChartType, related_name='rel_charts_charttypes')
    siteid = models.ForeignKey(Sites, related_name='rel_charts_sites')

    def render(self):
        #dang test truyen site vào render-> type content *.html
        #test ok
        print('model: render')
        if self.siteid_id == '123':
            print('profits: siteid %s' %{self.siteid_id})
            sites = Sites.objects.all()
            tables = Profits.objects.all()
            return render_to_string('menu/itemcontent/{}.html'.format(self._meta.model_name),
                                    {'item': self, 'sites': sites, 'tables':tables})
        else:
            print('budgets: siteid %s' %{self.siteid_id})
            sites = Sites.objects.all()
            tables = Budgets.objects.all()
            return render_to_string('menu/itemcontent/{}.html'.format(self._meta.model_name),
                                    {'item': self, 'sites': sites, 'tables':tables})


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