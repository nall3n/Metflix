from django.shortcuts import render, get_object_or_404

from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate

from movies.models import *

# Create your views here.



def index(request):
    pass

def media_player(request, id):
    pass