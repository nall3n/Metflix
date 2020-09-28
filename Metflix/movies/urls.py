# Movies URL conf
#========================


from . import views

from django.urls import path

app_name = 'movies'
urlpatterns = [
	path('', views.index, name='index'),
    path('episodes/<int:movie_id>/', views.episode_select, name='epsisode_select'),
    path('<int:movie_id>/', views.media_player, name='media_player'),
    path('<int:movie_id>/<int:season>/<int:episode>/', views.series_player, name = 'series_player'),

]
