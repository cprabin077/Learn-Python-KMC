from django.urls import path

from movie.views import category_list, movie_list

urlpatterns = [

    path('category_list/', category_list, name='category_list'),
    path('movie_list/', movie_list, name='movie_list'),
    # path('movie_create/', movie_create, name='create_movie'),
]
