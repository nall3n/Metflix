#==== MOVIE VIEWS ====

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


    context = {
        'movies': movies,
        'genres': genres
    }

    return render(request, 'movies/index.html', context)

def episode_select(request, id):
    pass

def media_player(request, id):
    
    movie = get_object_or_404(Movie, pk=id)

    for f in os.listdir(MEDIA_ROOT + movie.title):
        if f.endswith('.' + 'mp4'):
            movie_url = movie.title +'/' + f
        else:
            movie_url = 'No video file'
    
    movie_url = MEDIA_URL + movie_url

    context = {
        'movie_url': movie_url,
        'movie': movie,
    }

    return render(request, 'movies/media_player.html', context)


def series_player(request, movie_id, season, episode):
    pass

    context = {
        'test': 'Test'
    }
    return render(request, 'movies/media_player.html', context)
