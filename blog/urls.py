from django.conf.urls import patterns, url
from django.contrib.gis.views import feed

from blog.feeds import RSSFeed
from blog.views import archive

urlpatterns = patterns('',
                       url(r'^$', archive),
                       url(r'^feeds/(?P<url>.*)/$', feed,
                           {'feed_dict': {'rss': RSSFeed}}),
                       )
