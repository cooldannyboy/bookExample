#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from django.contrib import staticfiles

from django.conf.urls import patterns, include, url
from django.contrib import admin
from restaurants.views import menu, meta, restaurants_list, comment
from bookExample.views import welcome, set_c, get_c, session_test, index, register
#from bookExample.views import login, logout
from django.contrib.auth.views import login, logout

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
    url(r'^comment/(\d{1,5})/$', comment),
    url(r'^cookie/', set_c),
    url(r'^get_cookie/', get_c),
    url(r'^session/', session_test),
    url(r'^accounts/login/', login),
    url(r'^accounts/logout/', logout),
    url(r'^index/', index),
    url(r'^accounts/register/$', register)

)

#urlpatterns += staticfiles_urlpatterns()