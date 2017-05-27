from django.db import models
from django.db.models import Avg
from accounts.models import User
from django.utils import timezone

# Create your models here.

class Actor(models.Model):
    actor_name = models.CharField(max_length = 50)
    
    
class Director(models.Model):
    director_name = models.CharField(max_length = 50)
    
class Movie(models.Model):
    movie_name = models.CharField(max_length = 100)
    year = models.IntegerField()
    director = models.ForeignKey(Director,on_delete = models.CASCADE)
    movie_poster = models.ImageField(upload_to = 'media/movies/movie_poster', default = 'media/movies/movies_poster/no_cover.jpg')
    movie_by = models.ForeignKey(User,on_delete = models.CASCADE, related_name = 'movie_by')
    
    def getRating(self):
        rating = MovieRating.objects.filter(movie = self.id).aggregate(Avg('rate'))
        rate = rating['rate__avg']
        if rate == None:
            rate = 0
        return rate

    
class Movie_Actor(models.Model):
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE, related_name = 'movie_actor')
    actor = models.ForeignKey(Actor, on_delete = models.CASCADE, related_name = 'actor_movie')
    
    
class Movie_Genre(models.Model):
    GENRE = (('action','Action'),('adventure','Adventure'),('animation','Animation'),('biography','Biography'),('comedy','Comedy'),('crime','Crime'),('documentary','Documentary'),('drama','Drama'),('family','Family'),('fantasy','Fantasy'),('film-noir','Film-Noir'),('history','History'),('horror','Horror'),('music','Music'),('musical','Musical'),('mystery','Mystery'),('romance','Romance'),('sci-fi','Sci-Fi'),('sport','Sport'),('thriller','Thriller'),('war','War'),('western','Western'))
    movie =  models.ForeignKey(Movie, on_delete = models.CASCADE, related_name = 'movie_genre')
    genre = models.CharField(max_length = 30,choices = GENRE)
    
    
class MovieRating(models.Model):
    RATE = ((1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'))
    rate = models.IntegerField(choices = RATE)
    description = models.TextField()
    movie = models.ForeignKey(Movie,on_delete = models.CASCADE)
    booked_by = models.ForeignKey(User,on_delete = models.CASCADE, related_name = 'movie_rated_by')
    pub_date = models.DateTimeField(default=timezone.now)
