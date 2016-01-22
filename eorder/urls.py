from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from login.views import homepage

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eorder.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url('^$', homepage),
)
