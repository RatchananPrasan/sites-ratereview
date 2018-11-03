from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^register/$', views.register_view, name='register'),
    url(r'^profile/(?P<username>[\w.@+-]+)/$', views.profile_view, name='profile'),
    url(r'^profile/(?P<username>[\w.@+-]+)/post/$', views.profile_post, name='profile_post'),
    url(r'^reply/(?P<pk>[0-9]+)/$', views.post_reply, name='post_reply'),
    url(r'^settings/edit-profile/$', views.edit_profile, name='edit_profile'),
    url(r'^settings/change-password/$', views.change_password, name='change_password'),
    url(r'^settings/change-profile-pic/$', views.change_profile_pic, name='change_profile_pic'),
    url(r'^message/(?P<pk>[0-9]+)/delete/$', views.delete_message, name='message_delete'),
    url(r'^reply/(?P<pk>[0-9]+)/delete/$', views.delete_reply, name='reply_delete'),
    url(r'^api/', views.user_list),
]