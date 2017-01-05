from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from django.contrib import admin
from art_de_lex import settings
from art_de_lex import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'art_de_lex.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^ckeditor/', include('ckeditor_uploader.urls')),
	url(r'^$', views.index_list, name="index"),
	url(r'^', include('feedbacks.urls', namespace="feedbacks")),
	url(r'^', include('company.urls', namespace="company")),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
