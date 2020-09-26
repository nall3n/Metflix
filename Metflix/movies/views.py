from django.shortcuts import render, get_object_or_404

from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate

from movies.models import *

# Create your views here.

from Metflix.settings import MEDIA_ROOT, MEDIA_URL
import os

def index(request):
    
    movies = Movie.objects.all()
    genres = Genre.objects.all()



def media_player(request, id):
    
    movie = get_object_or_404(Movie, pk=id)

def series_player(request, movie_id, season, episode):
    pass
