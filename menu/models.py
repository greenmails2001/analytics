from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.db import models
# Create your models here.
from django.template.loader import render_to_string
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


class ItemContent(models.Model):
    menudetail = models.ForeignKey(MenuDetail, related_name='rel_itemcontents_menudetails')
    itemtype = models.ForeignKey(ContentType, limit_choices_to={'model__in':('text','video','image','file')})
    objid = models.PositiveIntegerField()
    item = GenericForeignKey('itemtype', 'objid')
    orderview = OrderField(blank=True, for_fields=['menudetail'])

    class Meta:
        ordering = ['orderview']

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
        return render_to_string('menu/itemcontent/{}.html'.format(self._meta.model_name), {'item': self})

class Text(ItemBase):
    content = models.TextField()

class File(ItemBase):
    file = models.FileField(upload_to='files')

class Image(ItemBase):
    file = models.FileField(upload_to='images')

class Video(ItemBase):
    url = models.URLField()
