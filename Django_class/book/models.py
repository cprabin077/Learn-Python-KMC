from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=150, unique=True, help_text="e.g Sci-Fi, Thriller, Crime, Drama ....", verbose_name="Genre Name")
    is_active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        db_table = "category"


class Book(models.Model):
    name = models.CharField(max_length=200, help_text="e.g Summer Love ...", verbose_name="Book Name")
    genre = models.ManyToManyField(Genre)
    language = models.CharField(max_length=50,null=True, blank=True)
    staring = models.CharField(max_length=1000, verbose_name="Characters Name")
    release_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        db_table = "book"

        
