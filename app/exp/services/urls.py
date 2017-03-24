from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^v1/$', views.index),
    url(r'^v1/experience/(?P<exp_id>[0-9]+)/$', views.experienceDetail),
    url(r'^v1/event/create/$', views.createEvent),
    url(r'^v1/signup/$', views.signUp),
    url(r'^v1/signin/$', views.signIn),
    url(r'^v1/checkUser/$', views.checkUserAuth)
]