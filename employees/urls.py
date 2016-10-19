from django.conf.urls import url
from employees import views


urlpatterns = [
    url(r'^register/$',
        views.EmployeeRegistrationView.as_view(), name='employee_registration'),
    url(r'^enroll-menuheader/$',
        views.EmployeeRequestMenuHeaderView.as_view(), name='employee_request_menuheader'),
    url(r'^menuheaders/$',
        views.EmployeeMenuHeaderListView.as_view(),name='employee_menuheader_list'),
    url(r'^menuheader/(?P<pk>\d+)/$',
        views.EmployeeMenuHeaderDetailView.as_view(),name='employee_menuheader_detail'),
    url(r'^menuheader/(?P<pk>\d+)/(?P<menudetail_id>\d+)/$',
        views.EmployeeMenuHeaderDetailView.as_view(),name='employee_menuheader_detail_menudetail'),
]
