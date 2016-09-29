from django.conf.urls import url

from . import views
app_name= 'enter'
urlpatterns = [


    url(r'^$', views.index, name='index'),

    url(r'^k/$', views.cost, name='cost'),
    url(r'^ch$', views.auth_view, name='auth_view'),

    url(r'^c$', views.loggedin, name='loggedin')

    ]