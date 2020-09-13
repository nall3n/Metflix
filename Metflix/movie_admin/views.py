from django.shortcuts import render, get_object_or_404

from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate

from movies.models import *

from Metflix.settings import MEDIA_ROOT, MEDIA_URL
import os

# Create your views here.

def index(request):

    movies = Movie.objects.all()
    genres = Genre.objects.all()

def add_movies(request):
    MOVIE_ROOT = os.path.join()

    # Check movie root dir for new movie folders
    # and adds them to database
    movie_list_dirs = os.listdir(MOVIE_ROOT)
    for movie in movie_list_dirs:
        # Check if movie alredy is in database
        # if so do not add movie
        try: 
            movie_db = Movie.objects.get(title = movie)
        except:
            m = Movie.objects.create(title = movie)
            m.save()
        else:
            print ('Movie excists')

    # Check al database entrys to the movie root dir 
    # if there is not dir with movie name 
    # Delete from database
    movie_list_db = Movie.objects.all()
    for movie in movie_list_db:
        if not os.path.isdir(os.path.join( MOVIE_ROOT, movie)):
            movie.delete()
