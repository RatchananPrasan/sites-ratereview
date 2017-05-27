from django.conf.urls import url
from . import views

app_name = 'recipes'

urlpatterns = [
    url(r'^search/$', views.recipe_search, name='search'),
    url(r'^create/$', views.recipe_create, name='create'),
    url(r'^view/(?P<pk>[0-9]+)/$', views.recipe_view, name='view'),
    url(r'^follow/(?P<following>[0-9]+)/(?P<recipe_id>[0-9]+)/$', views.recipe_follow, name='follow'),
    url(r'^unfollow/(?P<following>[0-9]+)/(?P<recipe_id>[0-9]+)/$', views.recipe_unfollow, name='unfollow'),
    url(r'^favourite/(?P<recipe_id>[0-9]+)/$', views.recipe_favourite, name='favourite'),
    url(r'^unfavourite/(?P<recipe_id>[0-9]+)/$', views.recipe_unfavourite, name='unfavourite'),
    url(r'^rate/(?P<recipe_id>[0-9]+)/$', views.recipe_rate, name='rate'),
]