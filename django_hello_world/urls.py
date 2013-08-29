from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'django_hello_world.hello.views.home', name='home'),
    # url(r'^django_hello_world/', include('django_hello_world.foo.urls')),

    url(r'last_requests/', 'django_hello_world.hello.views.requests', name='requests'),
    url(r'accounts/profile/', 'django_hello_world.hello.views.form', name='form'),
    #url(r'login/', 'django_hello_world.hello.views.login', name='login'),
    url(r'accounts/login/', 'django.contrib.auth.views.login', {'template_name': 'hello/login.html'}, name='login'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
