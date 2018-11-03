from rest_framework import serializers
from .models import Actor, Director, Movie,Movie_Actor,Movie_Genre,MovieRating

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        actor = Actor
        director = Director
        movie = Movie
        movie_actor = Movie_Actor
        movie_genre = Movie_Genre
        movie_rate = MovieRating
        fields = '__all__'
    