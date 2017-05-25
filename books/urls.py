from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'books'

urlpatterns = [
    url(r'^create/$',views.createNewBook, name = 'create_book'),
    url(r'^book/(?P<book_id>[0-9]+)/$',views.get_book_detail, name = "book_detail"),
    url(r'^search/(?P<search_key>[\w.+-]+)$',views.searchBook, name = "book_search"),
    url(r'^search/$',views.searching, name = "searching_for_book"),
    url(r'^browse/$',views.browseAllBooks,name = "browse_all_book"),
    url(r'^createNewRating/(?P<book_id>[0-9]+)/$',views.createNewBookRating,name = "create_new_book_rating")
]