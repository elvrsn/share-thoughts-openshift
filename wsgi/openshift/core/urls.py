from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView

urlpatterns = patterns('core.views',
    url(r'^$', 'home'),
    url(r'^search/$', 'search'),
    url(r'^article/$', 'article'),
    url(r'^share/$', 'toshare'),
    url(r'^about/$', 'about'),
    url(r'^thoughts/$', 'getthoughts'),
    url(r'^addthought/$', 'addthought'),
    url(r'^feedback/$', 'feedback'),
    url(r'^category/$', 'getcategory'),
    url(r'^thanks/$','thanks',name="thanks_page"),
    url(r'^feedback_thanks/$', 'feedback_thanks'),
    url(r'^sitemap/$',TemplateView.as_view(template_name="sitemap.html"))
)

