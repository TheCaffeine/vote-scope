from django.conf.urls import url
from Voters import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^county/$',views.countyApi),
    url(r'^county/([0-9]+)$',views.countyApi),

     url(r'^voter/$',views.voterApi),
    url(r'^voter/([0-9]+)$',views.voterApi),

    url(r'^SaveFile$', views.SaveFile)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)