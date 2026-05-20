from django import forms

from home.models import Student

class StudentForm(forms.ModelForm):
    # name = forms.CharField(widget=forms.NumberInput())
    # name = forms.CharField(widget=forms.PasswordInput())
    name = forms.CharField(widget=forms.TextInput())
    
    dob = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))

    class Meta:
        model = Student
        fields = '__all__'