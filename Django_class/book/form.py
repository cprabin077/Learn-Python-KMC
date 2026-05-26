from django import forms
from movie.models import Genre, Book 

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'

        
class BookForm(forms.ModelForm):
    
    class Meta:
        model = Book
        fields = '__all__'
        