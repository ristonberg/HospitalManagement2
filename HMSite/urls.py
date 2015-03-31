from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    url(r'HMS/', include ('HMS.urls')),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^sign_up/', ('HMS.views.register_user')),
    #url(r'^register_success/', ('HMS.views.register_success')),
    url(r'^confirm/(?P<activation_key>\w+)/', ('HMS.views.register_confirm')),
)
