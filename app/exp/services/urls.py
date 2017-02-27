from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^v1/$', views.index),
    url(r'^v1/experience/(?P<exp_id>[0-9]+)/$', views.experienceDetail),
]