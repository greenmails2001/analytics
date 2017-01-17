from django.db import models
'''
########Test########
Dynamically Add Form to Formset Using JavaScript and Django
http://stellarchariot.com/blog/2011/02/dynamically-add-form-to-formset-using-javascript-and-django/
'''
# Create your models here.
class TodoList(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class TodoItem(models.Model):
    name = models.CharField(max_length=150,
               help_text="e.g. Buy milk, wash dog etc")
    list = models.ForeignKey(TodoList)

    def __unicode__(self):
        return self.name + " (" + str(self.list) + ")"


#models.py
class VehicleBrand(models.Model):
    description = models.CharField(max_length=100)
    code = models.SlugField(primary_key=True)

class VehicleModel(models.Model):
    description = models.CharField(max_length=100)
    code = models.SlugField(primary_key=True)
    brand = models.ForeignKey(VehicleBrand)