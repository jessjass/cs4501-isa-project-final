from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^v1/event/(?P<event_id>[0-9]+)/$', views.eventById),
    url(r'^v1/event/image/(?P<event_id>[0-9]+)/$', views.eventImageById),
    url(r'^v1/event/experience/(?P<exp_id>[0-9]+)/$', views.eventByExpId),
    url(r'^v1/event/$', views.eventAll, name="event"),
    url(r'^v1/event/remove/$', views.remove),
    url(r'^v1/experience/(?P<exp_id>[0-9]+)/$', views.experienceById),
    url(r'^v1/experience/$', views.experienceAll),
    url(r'^v1/experience/remove/$', views.removeExperience),
    url(r'^v1/user/$', views.userAll),
    url(r'^v1/user/(?P<user_id>[0-9]+)/$', views.userById),
    url(r'^v1/user/experience/(?P<user_id>[0-9]+)/$', views.addExpUserById),
    url(r'^v1/user/event/(?P<user_id>[0-9]+)/$', views.addEventUserById),
    url(r'^v1/user/friend/(?P<user_id>[0-9]+)/$', views.addFriendUserById),
    url(r'^v1/user/remove/$', views.removeUser),
    url(r'^v1/user/check/$', views.checkUser),
    url(r'^v1/user/auth/$', views.getUserByAuth),
    url(r'^v1/auth/create/$', views.createAuth),
    url(r'^v1/auth/check/$', views.checkAuth),
    url(r'^v1/auth/remove/$', views.removeAuth)
]