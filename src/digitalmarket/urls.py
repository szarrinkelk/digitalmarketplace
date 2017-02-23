from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^detail/$', 'products.views.detail_view', name='detail_view'),
    url(r'^list/$', 'products.views.list_view', name='list_view'),
]
