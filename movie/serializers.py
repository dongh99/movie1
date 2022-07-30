from rest_framework import serializers
from dataclasses import field
from .models import Movie

class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title_kor','poster_url']

class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title_eng', 'rating_aud','rating_cri','genre','showtimes','release_date','rate','summary','name','role','image_url']
    