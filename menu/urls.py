from django.conf.urls import url

from menu import views

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
    url(r'^results/$', views.search, name='results'),
]