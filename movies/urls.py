from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'movies'

urlpatterns = [
    url(r'^create/$',views.createNewMovie, name = 'create_movie'),
    url(r'^movie/(?P<movie_id>[0-9]+)/$',views.get_movie_detail, name = "movie_detail"),
    url(r'^createNewRating/(?P<movie_id>[0-9]+)/$',views.createNewMovieRating,name = "create_new_movie_rating"),
    url(r'^browse/$',views.browseAllMovies, name = "browse_all_movie"),
    url(r'^search/(?P<search_key>.*)$',views.searchMovie, name = "movie_search"),
    url(r'^searchByPerson/(?P<search_key>.*)$',views.searchMovieByPerson, name = "movie_search_by_person"),
    url(r'^searchByGenre/(?P<search_key>.*)$',views.searchMovieByGenre, name = "movie_search_by_genre"),
    url(r'^search/$',views.searching, name = "searching_for_movie"),
    url(r'^deleteBook/(?P<movie_id>[0-9]+)/$',views.deleteMovie,name = "delete_movie"),


]
