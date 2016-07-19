from django.conf.urls import url

from . import views

app_name = 'manager'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<user_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<user_id>[0-9]+)/infocheck/$', views.infocheck, name='infocheck'),
    url(r'^(?P<user_id>[0-9]+)/devicecheck/$', views.devicecheck, name='devicecheck'),
    url('newuser/$', views.newuser, name='newuser'),
    url('addcompleted/$', views.addcompleted, name='addcompleted'),
]
