from django.conf.urls import url
from . import views

app_name = 'sites'

urlpatterns = [
    url(r'^home/$', views.sites_home_view, name='home'),
]