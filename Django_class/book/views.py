from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from book.models import Book, Genre


# Genre List
class GenreView(LoginRequiredMixin, ListView):
    model = Genre
    template_name = "genre/index.html"
    context_object_name = "genres"

# Genre Create
class GenreCreateView(LoginRequiredMixin, CreateView):
    model = Genre
    fields = "__all__"
    template_name = "genre/create.html"
    success_url = reverse_lazy("genre_list")


# Book List
class BookView(LoginRequiredMixin, ListView):
    model = Book
    template_name = "book/index.html"
    context_object_name = "books"


# Book Create
class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    fields = "__all__"
    template_name = "book/create.html"
    success_url = reverse_lazy("book_list")


# Book Update
class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    fields = "__all__"
    template_name = "book/update.html"
    success_url = reverse_lazy("book_list")


# Book Delete
class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = "book/delete.html"
    success_url = reverse_lazy("book_list")