from django.conf.urls import patterns, include, url
from company import views

urlpatterns = patterns('',
    url(r'^biography/(?P<employees_id>\d+)/$', views.employee_detail, name='employee_detail'),
	url(r'^services/(?P<services_id>\d+)/$', views.service_detail, name='service_detail'),
	url(r'^services/list/$', views.service_list, name='service_list'),
	
)

