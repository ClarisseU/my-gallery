from django.conf.urls import url, include
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.welcome, name = 'welcome'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^image/(?P<id>[\w-]+)/$', views.image, name='image'),
    url(r'^location/(?P<location>\D+)/$', views.location, name='location'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)