from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.index),
    url(r'^v1/events/(?P<event_id>[0-9]+)/$', views.eventById),
    url(r'^v1/events/experience/(?P<exp_id>[0-9]+)/$', views.eventByExpId),
    url(r'^v1/events/$', views.eventsAll),
    url(r'^v1/events/remove/$', views.remove),
    url(r'^v1/experience/(?P<experience_id>[0-9]+)/$', views.experienceById),
    url(r'^v1/experience/$', views.experienceAll),
    url(r'^v1/experience/remove/$', views.removeExperience),
    url(r'^v1/user/$', views.userAll),
    url(r'^v1/user/(?P<user_id>[0-9]+)/$', views.userById),
    url(r'^v1/user/experience/(?P<user_id>[0-9]+)/$', views.addExpUserById),
    url(r'^v1/user/remove/$', views.removeUser),

]