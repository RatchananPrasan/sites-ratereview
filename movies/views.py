from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.forms import formset_factory
from .forms import *
from .models import *
from .validateFormatTools import VFMovieTool

# Create your views here.

def createNewMovie(request):
    
    GenreFormSet = formset_factory(AddGenreForm, formset=BaseAddGenreFormset)
    is_genre_error = False
    
    ActorFormSet = formset_factory(AddActorForm, formset=BaseAddActorForm)
    is_actor_error = False
    
    if request.method == 'POST':
        form1 = CreateMovieForm(request.POST, request.FILES)
        genreforms = GenreFormSet(request.POST, prefix='genre')
        actorforms = ActorFormSet(request.POST, prefix='actor')
        if form1.is_valid():
            if genreforms.is_valid():
                if actorforms.is_valid():
                    wizard = VFMovieTool();
                    input_movie_name = form1.cleaned_data['movie_name']
                    input_year = form1.cleaned_data['year']
                    input_director = form1.cleaned_data['director']
                    input_poster_cover = form1.cleaned_data['movie_poster']
                    input_director = wizard.formatPersonName(input_director)

                    genre_list = []
                    for form in genreforms:
                        if form.cleaned_data:
                            temp_genre = form.cleaned_data['genre']
                            if temp_genre not in genre_list:
                                genre_list.append(temp_genre)
                                
                    actor_list = []
                    for form in actorforms:
                        if form.cleaned_data:
                            actor_list.append(form.cleaned_data['actor_name'])
                            
                    print("\t",actor_list)
                    print("\t",genre_list)
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
                    for genre in genre_list:
                        newGenre = Movie_Genre(movie = newMovie, genre = genre)
                        newGenre.save()
                    for people in actor_list:
                        peopled = wizard.formatPersonName(people)
                        try:
                            newActor = Actor.objects.get(actor_name = peopled )
                        except Actor.DoesNotExist:
                            newActor = Actor(actor_name = peopled)
                            newActor.save()
                        newMovieActor = Movie_Actor(movie = newMovie, actor = newActor)
                        newMovieActor.save()
                    return redirect('movies:movie_detail',newMovie.id)
                else:
                    is_actor_error = True
            else:
                is_genre_error = True
    
    actorforms= ActorFormSet(prefix='actor')
    genreforms = GenreFormSet(prefix='genre')
    form1 = CreateMovieForm()
    return render(request, 'movies/createMovie.html',{'form1':form1,'genreforms':genreforms,'is_genre_error':is_genre_error,'actorforms':actorforms,'is_actor_error':is_actor_error})

def get_movie_detail(request,movie_id):
    movie = get_object_or_404(Movie, pk = movie_id)
    print("in")
    print("\t",movie.getActorList())
    print("\t",movie.getGenreList())
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
    try :
        print("\t",1)
        theDirector = Director.objects.get(director_name = search_key)
        print("\t",2)
        movies = Movie.objects.filter(director = theDirector.id )
        print("\t",3)
    except Director.DoesNotExist:
        print("\t",4)
        theActor = Actor.objects.get(actor_name = search_key)
        print("\t",5)
        listActor = Movie_Actor.objects.filter(actor = theActor)
        print("\tsearch key",search_key)
        print("\t actor",theActor.actor_name)
        print("\t",6)
        movies = []
        for i in listActor:
            print("\t",i.movie.movie_name)
            movies.append(Movie.objects.get(pk = i.movie.id))
        print("\t",7)
    return render(request, 'movies/browse_page.html',{'movies':movies, 'movies_found':len(movies)})

def searchMovieByGenre(request,search_key):
    movieList = Movie_Genre.objects.filter(genre = search_key)
    movies = []
    for i in  movieList:
        movies.append(Movie.objects.get(pk = i.movie.id))
    return render(request, 'movies/browse_page.html',{'movies':movies, 'movies_found':len(movies)})    

def deleteMovie(request,movie_id):
    movie = Movie.objects.get(pk = movie_id)
    movie.delete()
    return redirect('movies:browse_all_movie')