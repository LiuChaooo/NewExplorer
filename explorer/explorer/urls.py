from django.conf.urls import include, url
from django.conf import settings
from django.views.static import serve as serve_static
from django.views.decorators.cache import never_cache
from .apps import welcome,api

urlpatterns = [
    url(r'^$', welcome.views.home),
    url(r'^block', welcome.views.home),
    url(r'^status', welcome.views.home),
    url(r'^address', welcome.views.home),
    url(r'^addrs', welcome.views.home),
    url(r'^tx', welcome.views.home),
    url(r'^contracts', welcome.views.home),
    url(r'^contract', welcome.views.home),
    url(r'^api/v(?P<version>[0-9]+)/', include('explorer.apps.api.urls')),
    url(r'^dashboard', api.apis.api_for_dashboard),
]

if settings.DEBUG:
    urlpatterns.append(url(r'^js/(?P<path>.*)$', never_cache(serve_static),
                                    {'document_root': '%s/templates/ui/public/js' % (settings.PROJECT_ROOT), 'show_indexes': True}))
    urlpatterns.append(url(r'^css/(?P<path>.*)$', never_cache(serve_static),
                                    {'document_root': '%s/templates/ui/public/css' % (settings.PROJECT_ROOT), 'show_indexes': True}))
    urlpatterns.append(url(r'^views/(?P<path>.*)$', never_cache(serve_static),
                                    {'document_root': '%s/templates/ui/public/views' % (settings.PROJECT_ROOT), 'show_indexes': True}))
    urlpatterns.append(url(r'^img/(?P<path>.*)$', never_cache(serve_static),
                                    {'document_root': '%s/templates/ui/public/img' % (settings.PROJECT_ROOT), 'show_indexes': True}))
    urlpatterns.append(url(r'^fonts/(?P<path>.*)$', never_cache(serve_static),
                                    {'document_root': '%s/templates/ui/public/fonts' % (settings.PROJECT_ROOT), 'show_indexes': True}))
    urlpatterns.append(url(r'^lib/(?P<path>.*)$', never_cache(serve_static),
                                    {'document_root': '%s/templates/ui/public/lib' % (settings.PROJECT_ROOT), 'show_indexes': True}))

