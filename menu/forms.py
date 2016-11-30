from django import forms
from django.forms.models import inlineformset_factory

from budgets.models import Sites, Budgets, Profits
from menu.models import MenuDetail, MenuHeader, ItemContent, Chart

MenuDetailFormSet = inlineformset_factory(MenuHeader, MenuDetail, fields=['name','description'], extra=1, can_delete=True)

def get_menu_choices(value):
    choices_tuple = []
    #if datatype == 'sitestable':
    ##############test ok###############
    #choices_tuple = [(field,field) for field in Sites._meta.get_all_field_names()]
    #tuple(enumerate(choices_tuple, 1))---> ((1,'abc'),(2,'ad'),(3,'acde'),...)
    #choices_tuple2=tuple((choices_tuple, choices_tuple))
    #print(choices_tuple)
    ######################################
    if value == 'sitestable':
        choices_tuple = [(field,field) for field in Sites._meta.get_all_field_names()]
    elif value == 'budgetstable':
        choices_tuple = [(field,field) for field in Budgets._meta.get_all_field_names()]
    elif value == 'profitstable':
        choices_tuple = [(field,field) for field in Profits._meta.get_all_field_names()]

    #choices_tuple = (
    #    ('b1', 'Option b1'),
    #    ('b2', 'Option b2'),
    #    ('b3', 'Option b3'),
    #)
    print(value)
    print(choices_tuple)
    #do your stuff
    return choices_tuple


MY_CHOICES = (
    ('1', 'Option aa1'),
    ('2', 'Option aa2'),
    ('3', 'Option aa3'),
)

#tam thoi k sử dung,
class ItemContentForm(forms.ModelForm):
    #def __init__(self, *args, **kwargs):
    #    super(ItemContent, self).__init__(*args, **kwargs)
    #    self.fields['teaching_group'].choices = ______ # code to generate choices here

    def __init__(self,  *args, **kwargs):
        super(ItemContentForm, self).__init__(*args, **kwargs)

        #self._meta.get_field_by_name('choices_f')[0]._choices =choices_tuple #lazy(get_menu_choices, list)()#choices_tuple# get_menu_choices()
        #self.fields['choices_f'].choices = ['z1','z2','z3','z4','z5']#choices_tuple
        ########chay ok########
        #self.fields['choices_f'] = forms.ChoiceField(choices = MY_CHOICES)
        print('datatype')
        print(self.fields['datatype'].label)#  Sites.sitename.title())
        self.fields['choices_f'] = forms.ChoiceField(choices = get_menu_choices('profitstable'))

    class Meta:
        #model = Chart
        fields = '__all__'
    #    #exclude = ()