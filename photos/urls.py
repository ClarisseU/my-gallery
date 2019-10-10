from django.conf.urls import url, include
from . import views
from django.contrib import admin

urlpatterns=[
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.welcome, name = 'welcome')
    url(r'^search/', views.search_results, name='search_results')
    url(r'^image/', views.image, name='image')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)