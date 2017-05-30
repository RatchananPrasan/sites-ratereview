from django import forms
from django.forms import TextInput, Select, ClearableFileInput, NumberInput, BaseFormSet, ModelForm, ValidationError
from .models import *

class CreateMovieForm(forms.Form):
    movie_name = forms.CharField(label = 'Movie Name', max_length = 50,widget = TextInput(attrs = {'class':'form-control','required':True,'placeholder':'Name...'}))
    
    year = forms.IntegerField(label = 'Year',widget = NumberInput(attrs = {'class':'form-control','required':True,'placeholder':'2017'}) )
    
    director  = forms.CharField(label = 'Director', max_length = 50,widget = TextInput(attrs = {'class':'form-control','required':True,'placeholder':'Director...'}))
    
    movie_poster = forms.ImageField(label = 'Movie Poster', widget=ClearableFileInput(attrs={'required':False,'style':'color:white;'}))
    
    
class AddGenreForm(ModelForm):
    class Meta:
        model = Movie_Genre
        fields = ['genre']
        widgets = {
            'genre': Select(attrs={'class':'form-control'})
        }
    
class BaseAddGenreFormset(BaseFormSet):
    
    def clean(self):
        if any(self.errors):
            return
        
        genres = []
        for form in self.forms:
            if form.cleaned_data:
                genres.append(form.cleaned_data['genre'])
                
        if not genres:
            raise ValidationError("Need at least one genre.")
            
            
class AddActorForm(ModelForm):
    class Meta:
        model = Actor
        fields = ['actor_name']
        widgets = {
            'actor_name': TextInput(attrs={'class':'form-control','required':False,'placeholder':'Actor/Actress...'})
        }
        
class BaseAddActorForm(BaseFormSet):
    
    def clean(self):
        if any(self.errors):
            return
        
        actors = []
        for form in self.forms:
            if form.cleaned_data:
                actors.append(form.cleaned_data['actor_name'])
                
        if not actors:
            raise ValidationError("Need at least one actor")