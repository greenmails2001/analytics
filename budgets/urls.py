from django.conf.urls import url
from budgets import views
from budgets.views import grafico, plotResults

urlpatterns = [
    url(r'^menuheaders/$',
        views.BudgetListView.as_view(),name='budget_menuheader_list'),
    url(r'^menuheader/(?P<pk>\d+)/$',
        views.BudgetDetailView.as_view(),name='budget_menuheader_detail'),
    url(r'^menuheader/(?P<pk>\d+)/(?P<menudetail_id>\d+)/$',
        views.BudgetDetailView.as_view(),name='budget_menuheader_detail_menudetail'),
    url(r'^menuheader/(?P<pk>\d+)/(?P<menudetail_id>\d+)/(?P<site_id>\d+)/$',
        views.BudgetDetailView.as_view(),name='budget_menuheader_detail_menudetail_filtersite'),
    url(r'^results/result.png$', views.plotResults,name='plotResults'),
]