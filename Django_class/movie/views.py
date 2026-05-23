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


def category_update(request, id):
    category = Category.objects.get(id = id)
    form = CategoryForm(instance=category)

    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)

        if form.is_valid():
            form.save()
            return redirect('category_list')
        else:
            print(form.errors)

    context={
            'form': form
    }
    return render(request, 'category/update.html',context) 


def category_delete(request, id):
    category = Category.objects.get(id=id).delete()
    return redirect('category_list')


# Movie
def movie_list(request):
    movie = Movie.objects.all()

    context = {
        "movie": movie
    }

    return render(request, 'movie/index.html', context)

def movie_create(request):
    form = MovieForm()
    category = Category.objects.all()

    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
        else:
            print(form.errors)

    context = {
        "form": form,
        "category": category
    }

    return render(request, 'movie/create.html', context)


def movie_update(request, id):
    movie = Movie.objects.get(id = id)
    form = MovieForm(instance=movie)
    category = Category.objects.all()
    
    if request.method == "POST":
        form = MovieForm(request.POST, instance=movie)

        if form.is_valid():
            form.save()
            return redirect('movie_list')
        else:
            print(form.errors)

    context={
            'form': form,
            "category": category
    }
    return render(request, 'movie/update.html',context) 


def movie_delete(request, id):
    movie = Movie.objects.get(id=id).delete()
    return redirect('movie_list')

