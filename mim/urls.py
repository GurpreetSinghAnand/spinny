from django.conf.urls import url

from mim import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login/$', views.login),
    url(r'^auth/$', views.auth_view),
    url(r'^logout/$', views.logout),
    url(r'^index/$', views.index),
    url(r'^products/$', views.products),
    url(r'^customers/$', views.customers),
    url(r'^transactions/$', views.transactions),
    url(r'^invalid/$', views.invalid_login),
]
