from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'LoL.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^',include('competition.urls', namespace="competition")),
    url(r'^admin/', include(admin.site.urls)),
)
