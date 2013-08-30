from django.conf.urls import patterns, include, url
import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django_hello_world.settings import MEDIA_ROOT

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'django_hello_world.hello.views.home', name='home'),
    # url(r'^django_hello_world/', include('django_hello_world.foo.urls')),

    url(r'last_requests/', 'django_hello_world.hello.views.requests', name='requests'),
    url(r'accounts/profile/', 'django_hello_world.hello.views.form', name='form'),
    #url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': MEDIA_ROOT,
        }),
    url(r'accounts/login/', 'django.contrib.auth.views.login', {'template_name': 'hello/login.html'}, name='login'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)


urlpatterns += patterns('django.contrib.staticfiles.views',
    url(r'^static/(?P<path>.*)$', 'serve'),
)

urlpatterns += staticfiles_urlpatterns()