from django import forms
from django.forms import ModelForm
from testapp.models import *


class TodoListForm(ModelForm):
  class Meta:
    model = TodoList
    fields = '__all__'


class TodoItemForm(ModelForm):
  class Meta:
    model = TodoItem
    fields = '__all__'
    #exclude = ('list',)

'''
class MyForm(forms.Form):
    original_field = forms.CharField()
    extra_field_count = forms.CharField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        extra_fields = kwargs.pop('extra', 0)

        super(MyForm, self).__init__(*args, **kwargs)
        self.fields['extra_field_count'].initial = extra_fields

        for index in range(int(extra_fields)):
            # generate extra fields in the number specified via extra_fields
            self.fields['extra_field_{index}'.format(index=index)] = \
                forms.CharField()
'''

class MyForm(forms.Form):

    empty_layer_name = forms.CharField(max_length=255, required=True, label="Name of new Layer")
    total_input_fields = forms.CharField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
      extra_fields = kwargs.pop('extra', 0)
      # check if extra_fields exist. If they don't exist assign 0 to them
      if not extra_fields:
         extra_fields = 0
      super(MyForm, self).__init__(*args, **kwargs)
      self.fields['total_input_fields'].initial = extra_fields
      for index in range(int(extra_fields)):
        # generate extra fields in the number specified via extra_fields
        self.fields['extra_field_{index}'.format(index=index)] = forms.CharField()