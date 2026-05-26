from django.urls import path

from book.views import BookCreateView, BookDeleteView, BookUpdateView, BookView, GenreCreateView, GenreView


urlpatterns = [
    path('genre/', GenreView.as_view(), name='genre_list'),
    path('genre/create/', GenreCreateView.as_view(), name='genre_create'),

    path('book/', BookView.as_view(), name='book_list'),
    path('book/create/', BookCreateView.as_view(), name='book_create'),
    path('book/update/<int:pk>/', BookUpdateView.as_view(), name='book_update'),
    path('book/delete/<int:pk>/', BookDeleteView.as_view(), name='book_delete'),
]
