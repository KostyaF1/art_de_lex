from django.conf.urls import patterns, include, url
from company import views

urlpatterns = patterns('',
    url(r'^biography/(?P<employees_id>\d+)/$', views.employee_detail, name='detail1'),
	url(r'^services/(?P<services_id>\d+)/$', views.service_detail, name='detail'),
	url(r'^services/list/$', views.service_list, name='list'),
	
)

