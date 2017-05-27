from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect

from .forms import *
from .models import *

# Create your views here.

def createNewMovie(request):
    
    
    
    form1 = CreateMovieForm()
    return render(request, 'movies/createMovie.html',{'form1':form1})
