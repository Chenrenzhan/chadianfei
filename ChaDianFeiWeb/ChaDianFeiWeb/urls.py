#!/home/talen/python2.7/bin/python
#coding=UTF8


from django.conf.urls import include, url
from django.contrib import admin

#from django.views.generic.simple import direct_to_template #旧版本，新版本不支持
from django.views.generic.base import TemplateView #django1.5之后

from ChaDianFei.views import *

urlpatterns = [
    # Examples:
    # url(r'^$', 'ChaDianFeiWeb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),

    url(r'^remark/$',remark),
    #url(r'^error/$',error),
    url(r'^message/$', TemplateView.as_view(template_name='index.html')),#Update
    url(r'^error/$', TemplateView.as_view(template_name='errorPage.html')),#Update
    url(r'^test.+',test),

]
