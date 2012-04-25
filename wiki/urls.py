from django.conf.urls import patterns, include, url

urlpatterns = patterns('wiki.views',
    url(r'^(?P<page_name>\w+)/edit/$', 'edit_page'),
    url(r'^(?P<page_name>\w+)/save/$', 'save_page'),
    url(r'^(?P<page_name>\w*)/$', 'view_page', name='view_page'),
)
