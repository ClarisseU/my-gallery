from django.conf.urls import url, include
from . import views
from django.contrib import admin

urlpatterns=[
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.welcome, name = 'welcome')
    url(r'^phtotos/', include(photos.urls))
]