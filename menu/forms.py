from django import forms
from django.forms.models import inlineformset_factory
from menu.models import MenuDetail, MenuHeader


MenuDetailFormSet = inlineformset_factory(MenuHeader, MenuDetail, fields=['name','description'], extra=1, can_delete=True)