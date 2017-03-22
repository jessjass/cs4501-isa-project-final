from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^signin/$', views.signIn, name='signIn'),
    url(r'^experience/(?P<exp_id>[0-9]+)/$', views.experienceDetail, name='experienceDetail'),
]