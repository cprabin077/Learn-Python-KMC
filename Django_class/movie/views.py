from django.shortcuts import render

from movie.models import Category, Movie

# Create your views here.
def movie_list(request):
    movies = Movie.objects.all()

    context = {
        "movies": movies
    }

    return render(request, 'movie/index.html', context)


def category_list(request):
    categories = Category.objects.all()

    context = {
        "categories": categories
    }

    return render(request, 'category/index.html', context)


# def movie_create(request):
#     movies = Movie.objects.
