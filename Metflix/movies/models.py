from django.db import models

# Create your models here.



class Movie(models.Model):
    title = models.CharField(max_length= 200)
    type = models.IntegerField() #Type 1 = Movie 2 = Series

    def __str__(self):
        return self.title


class Genre(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Genre_targets(models.Model):
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete = models.CASCADE)

    def __str__(self):
        return self.movie.title, self.genre.name


class Episode(models.Model):
    series = models.ForeignKey(Movie, on_delete= models.CASCADE)
    season = models.IntegerField()
    episode = models.IntegerField()
    path = models.CharField(max_lenght = 20)