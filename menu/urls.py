from django.conf.urls import url, patterns

from analytics import settings
from menu import views
from menu import plot

urlpatterns = [
    #tạm thoi rào lại, do cách tao url này copy từ ordershops, them vao se bi loi
    #url(r'^$',
    #    views.menufunction_dashboard, name='menufunction_dashboard'),
    #url(r'^(?P<menufunction_slug>[-\w]+)/$',
    #    views.menufunction_dashboard, name='menufunction_dashboard_by_category'),
    #url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
    #    views.menuheader_list, name='menuheader_list'),

    #mixin
    ##menuheader
    url(r'^mine/$',
        views.ManageMHListView.as_view(), name='manage_menuheader_list'),
    url(r'^create/$',
        views.MHCreateView.as_view(), name='menuheader_create'),
    url(r'^(?P<pk>\d+)/edit/$',
        views.MHUpdateView.as_view(), name='menuheader_edit'),
    url(r'^(?P<pk>\d+)/delete/$',
        views.MHDeleteView.as_view(), name='menuheader_delete'),
    ###menudetail
    url(r'^(?P<pk>\d+)/menudetail/$',
        views.MenuHeaderDetailUpdateView.as_view(),name='menuheader_menudetail_update'),
    ##itemcontent
    url(r'^menudetail/(?P<menudetail_id>\d+)/itemcontent/(?P<model_name>\w+)/create/$',
        views.ItemContentCreateUpdateView.as_view(), name='menudetail_itemcontent_create'),
    url(r'^menudetail/(?P<menudetail_id>\d+)/itemcontent/(?P<model_name>\w+)/(?P<id>\d+)/$',
        views.ItemContentCreateUpdateView.as_view(), name='menudetail_itemcontent_update'),
    url(r'^itemcontent/(?P<id>\d+)/delete/$',
        views.ItemContentDeleteView.as_view(), name='menudetail_itemcontent_delete'),
    url(r'^menudetail/(?P<menudetail_id>\d+)/$',
        views.MenuDetailItemContentListView.as_view(), name='menudetail_itemcontent_list'),
    #url(r'^menufunction/(?P<menufunction>[\w-]+)/$',
    #    views.MenuHeaderListView.as_view(), name='menuheader_list_menufunction'),
    url(r'^menufunction/(?P<slug>[\w-]+)/$',
        views.MainMenuListView.as_view(), name='mainmenu_list_menufunction'),
    url(r'^menufunction/(?P<slug>[\w-]+)/(?P<menuheader_id>\d+)/(?P<menudetail_id>\d+)/$',
        views.MainMenuListView.as_view(),name='mainmenu_list_menufunction_header_detail'),
    url(r'^menufunction/(?P<slug>[\w-]+)/(?P<menuheader_id>\d+)/(?P<menudetail_id>\d+)/(?P<site_id>\d+)/$',
        views.MainMenuListView.as_view(),name='mainmenu_list_menufunction_header_detail_filtersite'),
    url(r'^(?P<slug>[\w-]+)/$',
        views.MenuHeaderDetailView.as_view(), name='menuheader_detail'),
    url(r'^results/(?P<site_id>\d+)result.png$', views.plotResults,name='plotResults'),
    #url(r'^results/plot_profits_barline_(?P<site_id>\d+).png$', plot.plot_profits_barline,name='plot_profits_barline'),
    url(r'^results/plot_profits_barline_(?P<site_id>\d+).png$', plot.PlotView.plot_profits_barline,name='plot_profits_barline'),
    url(r'^results/plot_profits_line_(?P<site_id>\d+).png$', plot.PlotView.plot_profits_line,name='plot_profits_line'),
    url(r'^results/plot_revenues_line_(?P<site_id>\d+).png$', plot.PlotView.plot_revenues_line,name='plot_revenues_line'),
    #test django-chartit
    url(r'^results', plot.weather_chart_view.as_view(), name='weather_chart_view'),
    url(r'^budgets', plot.budget_chart_view.as_view(), name='budget_chart_view'),
    url(r'^profits/(?P<site_id>[\w-]+)/$', plot.profit_chart_view.as_view(), name='profit_chart_view'),
    url(r'^results/$', views.search, name='results'),
    #url(r'^(?P<filename>[^/]+)/$', views.file_serve, name='upload_file_serve'), #20161208 test fail
]
urlpatterns += patterns('menu.views',
                        url(r'^{0}(?P<path>.*)$'.format(settings.PRIVATE_MEDIA_URL.lstrip('/')), 'serve_private_file',), )