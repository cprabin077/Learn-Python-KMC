from django.contrib import admin

from home.models import Student

# Register your models here.
# admin.site.register(Student)

@admin.register(Student)
class Student_admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'dob', 'number', 'is_active']
    search_fields = ['name', 'dob']
    list_filter = ['is_active','name']