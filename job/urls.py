from django.conf.urls import url
from . import views

app_name = 'job'

urlpatterns = [
    url(r'^home/$', views.Home.as_view(), name='home'),
    url(r'^result/(?P<pk>[0-9]+)/$', views.result, name='result'),
]