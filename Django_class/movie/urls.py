from django.urls import path

from movie.views import category_create, category_delete, category_list, category_update, movie_create, movie_delete, movie_list, movie_update

urlpatterns = [
    # Category
    path('category_list/', category_list, name='category_list'),
    path('category_create/', category_create, name='category_create'),
    path('category_update/<id>/', category_update, name='category_update'),
    path('category_delete/<id>', category_delete, name='category_delete'),


    # Movie
    path('movie_list/', movie_list, name='movie_list'),
    path('movie_create/', movie_create, name='movie_create'),
    path('movie_update/<id>/', movie_update, name='movie_update'),
    path('movie_delete/<id>', movie_delete, name='movie_delete'),

]
