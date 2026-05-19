from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from home.models import Student

# Create your views here.
def home(request):
    print("Hello from  Django!!")
    return HttpResponse("<h1> Hello from  Django!! </h1>")


def home_json(request):
    data = {
        "name": "Prabin Chaudhary",
        "address": "Kathmandu"
    }
    return JsonResponse(data)


def home_page(request):
    # user_info = {
    #     'name':'Prabin Chaudhary'
    # }
    return render(request, "home/index.html")


def student_list(request):
    student = Student.objects.all()
    context = {
        "student": student
    }
    return render(request,'student/index.html', context)

