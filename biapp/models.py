from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.
from smart_selects.db_fields import ChainedForeignKey


class DataType(models.Model):
    id = models.CharField(max_length=20,primary_key=True)
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


class ColumnList(models.Model):
    id = models.CharField(max_length=20,primary_key=True)
    name = models.CharField(max_length=50, db_index=True)
    datatype = models.ForeignKey(DataType, related_name='rel_columnlists_datatypes')
    slug = models.SlugField(max_length=50, db_index=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        #return self.name
        return '{}- {}'.format(self.id, self.name)

    def get_absolute_url(self):
        return reverse('menu:column_list', args=[self.id, self.slug])

class Combine(models.Model):
    datatype = models.ForeignKey(DataType)
    columnlist = ChainedForeignKey(ColumnList, chained_field='datatype',
                                chained_model_field='datatype', show_all=False, auto_choose=True)

class ChartType(models.Model):
    id = models.CharField(max_length=20,primary_key=True)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    datatype = models.ForeignKey(DataType, related_name='rel_charttypes_datatypes')
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


class ReportList(models.Model):
    id = models.CharField(max_length=20,primary_key=True)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='image/reportlist/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        #return self.name
        return '{}. {}'.format(self.id, self.name)

    def get_absolute_url(self):
        return reverse('menu:charttype_list', args=[self.id, self.slug])
