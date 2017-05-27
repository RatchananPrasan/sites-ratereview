from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'movies'

urlpatterns = [
    url(r'^create/$',views.createNewMovie, name = 'create_movie'),

]
