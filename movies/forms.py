from django import forms
from django.forms import TextInput, Select, ClearableFileInput, NumberInput
from .models import *

class CreateMovieForm(forms.Form):
    movie_name = forms.CharField(label = 'Movie Name', max_length = 50,widget = TextInput(attrs = {'class':'form-control','required':True,'placeholder':'Name...'}))
    
    year = forms.IntegerField(label = 'Year',widget = NumberInput(attrs = {'class':'form-control','required':True,'placeholder':'2017'}) )
    
    director  = forms.CharField(label = 'Director', max_length = 50,widget = TextInput(attrs = {'class':'form-control','required':True,'placeholder':'Director...'}))
    
    movie_poster = forms.ImageField(label = 'Movie Poster', widget=ClearableFileInput(attrs={'required':False,'style':'color:white;'}))
    
    
class AddActorToMovie(forms.Form):
    actor  = forms.CharField(label = 'Actor/Actress', max_length = 50,widget = TextInput(attrs = {'class':'form-control','required':False, 'placeholder':'Actor/Actress...'}))
    
    
class AddGenreToMovie(forms.Form):
    choiceList = Movie_Genre.GENRE
    genre = forms.ChoiceField(label = 'Genre',choices = choiceList, widget=Select(attrs={'class':'form-control','required':False}))
