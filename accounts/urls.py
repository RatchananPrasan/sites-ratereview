from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^login/$', views.accounts_login_view, name='login'),
    url(r'^logout/$', views.accounts_logout_view, name='logout'),
    url(r'^register/$', views.accounts_register_view, name='register'),
]