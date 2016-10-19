from django import forms

from menu.models import MenuHeader


class MenuHeaderRequestForm(forms.Form):
    menuheader = forms.ModelChoiceField(
            queryset=MenuHeader.objects.all(),
            widget=forms.HiddenInput)