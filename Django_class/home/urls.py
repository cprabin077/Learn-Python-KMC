from home.views import home, home_json, home_page, student_create, student_create2, student_delete, student_list, student_update
from django.urls import path


urlpatterns = [
    path('', home, name='home'),
    path('json/', home_json, name='json-data'),
    path('home_page/',home_page, name = 'page'),
    path('student_list/', student_list, name="student"),
    path('student_create/', student_create, name="create"),
    path('student_create2/', student_create2, name="create2"),
    path('student_update/<int:id>/', student_update, name="update"),
    path('student_delete/<int:id>/', student_delete, name="delete"),
]
