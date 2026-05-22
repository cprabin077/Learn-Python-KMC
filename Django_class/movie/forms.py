from django import forms

from movie.models import Category, Movie 



class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

        
class MovieForm(forms.ModelForm):
    
    class Meta:
        model = Movie
        fields = '__all__'
        


