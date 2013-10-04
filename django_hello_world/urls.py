from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.views.generic import TemplateView

from django_hello_world.settings import MEDIA_ROOT


admin.autodiscover()

js_info_dict = {
    'packages': ('django.conf',),
}
urlpatterns = patterns('django_hello_world.hello.views',
    url(r'^$', 'home', name='home'),
    url(r'^last_requests/$', 'requests', name='requests'),
    url(r'^accounts/profile/$', 'form', name='form'),
    url(r'^success/$', TemplateView.as_view(template_name='hello/success.html'), name="contact_success"),
    url(r'^decrease_priority/(\d+)/$', 'decrease_priority', name='decrease_priority'),
    url(r'^increase_priority/(\d+)/$', 'increase_priority', name='increase_priority'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('django.views.i18n',
        (r'^jsi18n$', 'javascript_catalog', js_info_dict),
)

urlpatterns += patterns('django.contrib.staticfiles.views',
    url(r'^static/(?P<path>.*)$', 'serve'),
)

urlpatterns += staticfiles_urlpatterns()

urlpatterns += patterns('django.views',
    #url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^media/(?P<path>.*)$', 'static.serve', {'document_root': MEDIA_ROOT}),
)

urlpatterns += patterns('django.contrib.auth',
    url(r'^accounts/login/$', 'views.login', {'template_name': 'hello/login.html'}, name='login'),
)