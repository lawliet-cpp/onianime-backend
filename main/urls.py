from django.urls import path
from .scrapper import *

urlpatterns = [
    path('api/search',anime_watch,name="anime-watch"),
    path('api/download',anime_dowload,name="anime-download")

]