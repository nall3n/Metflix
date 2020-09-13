# Movie_admin URL Conf
#========================


from . import views

from django.urls import path

app_name = 'movie_admin'
urlpatterns = [
	path('', views.index, name='index'),
    path('add_movies', views.add_movies, name='add_movies'),
	
]
