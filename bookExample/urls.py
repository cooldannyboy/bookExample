from django.conf.urls import patterns, include, url
from django.contrib import admin
from restaurants.views import menu, meta, restaurants_list
from bookExample.views import welcome

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bookExample.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^menu/$', menu),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^meta/', meta),
    url(r'^welcome/$', welcome),
    url(r'^restaurants_list/$', restaurants_list),

)
