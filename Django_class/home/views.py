from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse

from home.forms import StudentForm
from home.models import Student
from django.contrib.auth.decorators import login_required

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

@login_required
def student_list(request):
    student = Student.objects.all()
    context = {
        "student": student
    }
    return render(request,'student/index.html', context)


def student_create(request):
    if request.method == "POST":
        print(request.method)
        data = request.POST
        Student.objects.create(
            name = data['student_name'],
            number = data['number'],
            dob = data['dob']
        )
        # print("This is POST method")
        return redirect('/home/student_list')
    return render(request, "student/create.html")

@login_required
def student_create2(request):
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/student_list')
        else:
            print(form.errors)    

    context = {
        'form': form
    }
    return render(request, "student/create2.html", context)


def student_update(request, id):
    student = Student.objects.get(id = id)
    form = StudentForm(instance=student)
    if request.method == "POST":
        form = StudentForm(data=request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('/home/student_list')
        else:
            print(form.errors)    

    context = {
        'form': form
    }

    return render(request, "student/update.html",{"form":form})


def student_delete(request, id):
    student = Student.objects.filter(id = id).delete()
    return redirect('/home/student_list')


