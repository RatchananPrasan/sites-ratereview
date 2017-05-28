from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect

from .forms import *
from .models import *
from .validateFormatTools import VFMovieTool

# Create your views here.

def createNewMovie(request):
    
    if request.method == 'POST':
        form1 = CreateMovieForm(request.POST, request.FILES)
        if form1.is_valid():
            wizard = VFMovieTool();
            input_movie_name = form1.cleaned_data['movie_name']
            input_year = form1.cleaned_data['year']
            input_director = form1.cleaned_data['director']
            input_poster_cover = form1.cleaned_data['movie_poster']
            input_director = wizard.formatPersonName(input_director)
            print("\t",input_movie_name)
            print("\t",input_year)
            print("\t",input_director)
            try:
                direct = Director.objects.get(director_name = input_director )
            except Director.DoesNotExist:
                direct = Director(director_name = input_director)
                direct.save()
            newMovie = Movie(movie_name = input_movie_name, year = input_year, director = direct, movie_poster = input_poster_cover, movie_by = request.user)
            newMovie.save()
            return redirect('movies:movie_detail',newMovie.id)
    
    
    
    form1 = CreateMovieForm()
    formGenre = AddGenreToMovie()
    return render(request, 'movies/createMovie.html',{'form1':form1,"form_genre":formGenre})

def get_movie_detail(request,movie_id):
    movie = get_object_or_404(Movie, pk = movie_id)
    try:
        ratedPost = MovieRating.objects.filter(movie = movie_id).order_by('-pub_date')
        return render(request,'movies/movie_detail.html',{'movie':movie,'ratedPost':ratedPost})
    except:
        return render(request,'movies/movie_detail.html',{'movie':movie,'ratedPost':None})
    

def createNewMovieRating(request, movie_id):
    if request.method == 'POST':
        try:
            rating = request.POST.get('rated_score')
            if rating is None:
                raise ValueError
            comment = request.POST.get('comment')
            movie = Movie.objects.get(pk = movie_id)
            newMovieRate = MovieRating( rate = rating, description = comment, movie = movie, booked_by = request.user)
            newMovieRate.save()
        except ValueError:
            pass
    
    return redirect('movies:movie_detail',movie_id)


def browseAllMovies(request):
    movies = Movie.objects.all()
    return render(request,'movies/browse_page.html',{'movies':movies,'movies_found':len(movies)})


def searching(request):
    s = request.GET['search_key']
    sk = "+".join(s.split())
    if sk != '':
        return redirect('movies:movie_search',sk)
    else:
        movies = Movie.objects.all()
        return render(request, 'movies/browse_page.html',{'movies':movies})



def searchMovie(request,search_key):
    search_key = " ".join(search_key.split('+'))
    movies = Movie.objects.filter(movie_name__icontains =  search_key)
    return render(request, 'movies/browse_page.html',{'movies':movies, 'movies_found':len(movies)})


def searchMovieByPerson(request,search_key):
    theDirector = Director.objects.get(director_name = search_key)
    theActor = Actor.objects.filter(actor_name = search_key)
    listActor = Movie_Actor.objects.filter(actor = theActor.id)
    movies = Movie.objects.filter(director = theDirector.id )
    for i in listActor:
        movies = movies | Movie.objects.filter(pk = i.movie.id)
    return render(request, 'movies/browse_page.html',{'movies':movies, 'movies_found':len(movies)})

