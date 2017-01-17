from django.conf.urls import url

from testapp.views import *

urlpatterns = [
    #url(r'^results', plot.weather_chart_view.as_view(), name='weather_chart_view'),
    #url(r'^budgets', plot.budget_chart_view.as_view(), name='budget_chart_view'),
    #url(r'^todo', index, name='index'),
    url(r'^todo2', myview, name='myview'),
    url(r'^brand/(?P<brand>[-\w]+)/all_json_models/', all_json_models, name='all_json_models'),
]