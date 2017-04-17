from django.conf.urls import url
from . import views

app_name = 'sites'

urlpatterns = [
    url(r'^home/$', views.sites_home_view, name='home'),
    url(r'^about/$', views.sites_about_view, name='about'),
    url(r'^content/$', views.sites_content_view, name='content')
]