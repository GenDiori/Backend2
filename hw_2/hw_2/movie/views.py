from django.http import JsonResponse
from .models import Movie

def movie_list(request):
    movies = list(Movie.objects.values())
    return JsonResponse(movies, safe=False)

def movie_detail(request, id):
    movie = Movie.objects.filter(id=id).values().first()
    return JsonResponse(movie, safe=False)
