from django.shortcuts import render
from .data.Blkom import Blkom
from .data.AnimeLek import Animelek
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(["GET"])
def anime_watch(request):
    anime_name = request.query_params.get('query')
    episode = request.query_params.get('episode')

    Anime_provider = Blkom('naruto', 1)

    anime_data = Anime_provider.get_anime_watch_link(anime_name, episode)

    return Response({
        "data": anime_data
    })


@api_view(["GET"])
def anime_dowload(request):
    anime_name = request.query_params.get('query')
    episode = request.query_params.get('episode')

    Anime_provider = Animelek(anime_name)

    anime_data = Anime_provider.get_download_link(episode)

    return Response({
        "data":anime_data
    })

    

