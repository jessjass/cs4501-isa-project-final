from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^experience/(?P<exp_id>[0-9]+)/$', views.experienceDetail, name='experienceDetail'),
    url(r'^event/create/$', views.createEvent, name='createEvent'),
    url(r'^signin/$', views.signIn, name='signIn'),
    url(r'^signup/$', views.signUp, name='signUp'),
    url(r'^signout/$', views.signOut, name='signOut'),
    url(r'^user/dashboard/$', views.userDashboard, name='userDashboard'),
    url(r'^event/search/$', views.searchEvents, name='searchEvents'),
]