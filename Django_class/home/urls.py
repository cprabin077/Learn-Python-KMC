from home.views import home, home_json, home_page, student_create, student_list
from django.urls import path


urlpatterns = [
    path('home/', home, name='home'),
    path('json/', home_json, name='json-data'),
    path('home_page/',home_page, name = 'page'),
    path('student_list/', student_list, name="student"),
    path('student_create/', student_create, name="create")

]
