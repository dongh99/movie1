from django.shortcuts import render, redirect
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import HttpResponse
from django.core.paginator import Paginator
from .serializers import HomeSerializer, MovieDetailSerializer, StaffDetailSerializer
from rest_framework.response import Response


import requests

@api_view(['GET'])
def init_db(request):
    url = "https://334e6eae-a450-4bd1-93ba-cd6f24271194.mock.pstmn.io/movie/movielist"
    res = requests.get(url)
    movies = res.json()['movies']
    print(movies)
    for movie in movies:
        one_movie = Movie()
        one_movie.title_kor = movie['title_kor']
        one_movie.title_eng = movie['title_eng']
        one_movie.poster_url = movie['poster_url']
        one_movie.rating_aud = movie['rating_aud']
        one_movie.rating_cri = movie['rating_cri']
        one_movie.genre = movie['genre']
        one_movie.showtimes = movie['showtimes']
        one_movie.release_date = movie['release_date']
        one_movie.rate = movie['rate']
        one_movie.summary = movie['summary']
        one_movie.save()

        staffs = movie['staff']
    
        for staff in staffs:
            one_staff = Staff()
            one_staff.movie = one_movie
            one_staff.name = staff['name']
            one_staff.role = staff['role']
            one_staff.image_url = staff['image_url']
            one_staff.save()

    #return Response(status=status.HTTP_200_OK)
    
    return redirect('home')

@api_view(['GET'])
def home(request):
    movies = Movie.objects.all()
    serializer = HomeSerializer(movies, many = True)
    paginator = Paginator(movies, 8)
    page = request.GET.get('page')
    paginated_movies = paginator.get_page(page)
    query = request.GET.get('query')
    if query:
        movies = Movie.objects.filter(title__contains=query)
    return Response(serializer.data)

@api_view(['GET'])
def detail(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
        #staff = Staff.objects.get(pk=pk)
        serializer1 = MovieDetailSerializer(movie)
        #serializer2 = StaffDetailSerializer(staff)
        return Response(serializer1.data)
    except Staff.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)