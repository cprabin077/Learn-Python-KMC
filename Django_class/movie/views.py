from django.shortcuts import redirect, render

from movie.forms import CategoryForm, MovieForm
from movie.models import Category, Movie

# Create your views here.

# Category
def category_list(request):
    category = Category.objects.all()

    context = {
        "category": category
    }

    return render(request, 'category/index.html', context)


def category_create(request):
    category = CategoryForm()

    if request.method == 'POST':
        category = CategoryForm(data=request.POST)
        if category.is_valid():
            category.save()
            return redirect('category_list')
        else:
            print(category.errors)

    context = {
        "category": category
    }
    return render(request, 'category/create.html', context)


# Movie
def movie_list(request):
    movie = Movie.objects.all()

    context = {
        "movie": movie
    }

    return render(request, 'movie/index.html', context)

def movie_create(request):
    movie = MovieForm()
    category = Category.objects.all()

    if request.method == 'POST':
        movie = MovieForm(data=request.POST)
        if movie.is_valid():
            movie.save()
            return redirect('movie_list')
        else:
            print(movie.errors)

    context = {
        "movie": movie,
        "category": category
    }

    return render(request, 'movie/create.html', context)

