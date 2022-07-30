from django.db import models
from django.forms import CharField

class Movie(models.Model):
    title_kor = models.CharField(max_length=100, null=True)
    title_eng = models.CharField(max_length=100, null=True)
    poster_url = models.URLField(max_length=100, null=True)
    rating_aud = models.CharField(max_length=100, null=True)
    rating_cri = models.CharField(max_length=100, null=True)
    genre = models.CharField(max_length=100, null=True)
    showtimes = models.CharField(max_length=100, null=True)
    release_date = models.CharField(max_length=100, null=True)
    rate = models.CharField(max_length=100, null=True)
    summary = models.CharField(max_length=500, null=True)
        
    def __str__(self):
        return self.title

class Staff(models.Model):
    movie = models.ForeignKey(Movie, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    role = models.CharField(max_length=100, null=True)
    image_url = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.title