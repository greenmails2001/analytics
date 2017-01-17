from django.forms import BaseFormSet, formset_factory
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template.context_processors import csrf

from testapp.forms import *


def index(request):
    # This class is used to make empty formset forms required
    # See http://stackoverflow.com/questions/2406537/django-formsets-make-first-required/4951032#4951032
    class RequiredFormSet(BaseFormSet):
        def __init__(self, *args, **kwargs):
            super(RequiredFormSet, self).__init__(*args, **kwargs)
            for form in self.forms:
                form.empty_permitted = False
    TodoItemFormSet = formset_factory(TodoItemForm, max_num=10, formset=RequiredFormSet)
    if request.method == 'POST': # If the form has been submitted...
        todo_list_form = TodoListForm(request.POST) # A form bound to the POST data
        # Create a formset from the submitted data
        todo_item_formset = TodoItemFormSet(request.POST, request.FILES)

        if todo_list_form.is_valid() and todo_item_formset.is_valid():
            todo_list = todo_list_form.save()
            for form in todo_item_formset.forms:
                todo_item = form.save(commit=False)
                todo_item.list = todo_list
                todo_item.save()
            #return HttpResponseRedirect('thanks') # Redirect to a 'success' page
            return HttpResponse('Thanks')
    else:
        todo_list_form = TodoListForm()
        todo_item_formset = TodoItemFormSet()

    # For CSRF protection
    # See http://docs.djangoproject.com/en/dev/ref/contrib/csrf/
    c = {'todo_list_form': todo_list_form,
         'todo_item_formset': todo_item_formset,
        }
    c.update(csrf(request))

    return render_to_response('testapp/index.html', c)


def myview(request):
    if request.method == 'POST':
        form = MyForm(request.POST, extra=request.POST.get('total_field_count'))
        if form.is_valid():
            print("valid!")
    else:
        form = MyForm()
    return render(request, 'testapp/addfield.html', { 'form': form })


#views.py,all_json_models
def all_json_models(request, brand):
    current_brand = VehicleBrand.objects.get(code=brand)
    models = VehicleModel.objects.all().filter(brand=current_brand)
    from django.core import serializers
    import json
    json_models = serializers.serialize("json", models)
    #struct = json.loads(json_models)
    #json_models = json.dumps(struct[0])
    return HttpResponse(json_models, content_type="application/javascript")

