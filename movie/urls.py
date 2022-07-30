from django.urls import path
from .views import *

app_name = 'movie'

urlpatterns = [
    path('', init_db),
    path('home', home),
    path('<int:pk>/', detail),
]