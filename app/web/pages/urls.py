from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^signinpage/$', views.signInPage, name='signInPage'),
    url(r'^experience/(?P<exp_id>[0-9]+)/$', views.experienceDetail, name='experienceDetail'),
    url(r'^event/create/$', views.createEvent, name='createEvent'),
    url(r'^signin/$', views.signIn, name='signIn'),
]