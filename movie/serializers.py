from rest_framework import serializers
from dataclasses import field
from .models import *

class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title_kor','poster_url']

class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title_eng', 'rating_aud','rating_cri','genre','showtimes','release_date','rate','summary']

class StaffDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ['movie', 'name','role','image_url']
    