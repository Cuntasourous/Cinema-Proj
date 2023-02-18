from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Genre(models.Model):
    genre_name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.genre_name

class Movie_list(models.Model):
    movie_title = models.CharField(max_length=100, unique=True)
    poster = models.ImageField(upload_to='media/posters/')
    genre_1 = models.ForeignKey(Genre, on_delete=models.CASCADE)
    #genre_2 = models.ForeignKey(Genre, on_delete=models.CASCADE)
    #genre_3 = models.ForeignKey(Genre, on_delete=models.CASCADE)
    release_year = models.DateField()
    runtime = models.DurationField()
    rating = models.FloatField(max_length=3)
    director = models.CharField(max_length=100)
    age_restrict = models.CharField(max_length=5)
    plot = models.TextField()
    wallpaper = models.ImageField(upload_to='media/wallpapers/')

    def __str__(self):
        return self.movie_title

    def get_year(self):
        return self.release_year.strftime('%Y')

class timeslots(models.Model):
    timeslot_1 = models.CharField(max_length=10)

    def __str__(self):
        return self.timeslot_1

class book(models.Model):
    movie_title = models.ForeignKey(Movie_list, on_delete=models.CASCADE)
    seats = models.IntegerField(default=1)
    date = models.DateField(default='2023-01-01')
    time = models.ForeignKey(timeslots, on_delete=models.CASCADE)
   #user

    def __str__(self):
        return str(self.date)

class book2(models.Model):
    movie_title = models.ForeignKey(Movie_list, on_delete=models.CASCADE)
    seats = models.IntegerField(default=1)
    date = models.DateField(default='2023-01-01')
    time = models.ForeignKey(timeslots, on_delete=models.CASCADE)
    #user

    def __str__(self):
        return self.movie_title

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #password = models.CharField(widget=models.passwordInput())
    #additional classes
    #portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username 

class book3(models.Model):
    movie_title = models.CharField(max_length=100)
    seats = models.IntegerField(default=1)
    date = models.DateField(default='2023-01-01')
    time = models.ForeignKey(timeslots, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.movie_title + " by " + str(self.user)

    def get_absolute_url(self):
        return reverse('show_book', args=(str(self.id)))

