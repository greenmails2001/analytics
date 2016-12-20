"""analytics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views

from menu import views
from menu.views import MenuHeaderListView, MainMenuListView, homepage

urlpatterns = [

    #url(r'^accounts/login/$', auth_views.login, name='login'),
    #url(r'^accounts/logout/$', auth_views.logout, name='logout'),
    #url(r'^accounts/profile/$', auth_views.login, name='user_profile'),
    url(r'^account/', include('account.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('menu.urls', namespace='menu')),
    url(r'^menuheader/', include('menu.urls')),
    #url(r'^$', MenuHeaderListView.as_view(), name='menuheader_list'),
    url(r'^$', views.homepage, name='homepage'),
    url(r'^employees/', include('employees.urls')),
    url(r'^budgets/', include('budgets.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
