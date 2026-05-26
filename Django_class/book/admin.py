from django.contrib import admin

# Register your models here.
from book.models import Book, Genre

# Register your models here.
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields =['name']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name','release_date','language','staring']
    autocomplete_fields = ['genre']
