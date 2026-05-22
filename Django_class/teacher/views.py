from django.shortcuts import redirect, render

from teacher.forms import TeacherForm
from teacher.models import Teacher

# Create your views here.

# diaplay all the list of teacher
def teacher_list(request):
    data = Teacher.objects.all()
    context = {
        "teacher":data
    }
    return render(request, 'teacher/index.html', context)

# create a new teacher
def teacher_create(request):
    form = TeacherForm()

    if request.method == "POST":
        form = TeacherForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('teacher')   # use URL name
        else:
            print(form.errors)   # IMPORTANT
    context =  {
        'form': form
    }
    return render(request, 'teacher/create.html',context)

# update the data of teacher
def teacher_update(request, id):
    teacher = Teacher.objects.get(id=id)
    form = TeacherForm(instance=teacher)

    if request.method == "POST":
        form = TeacherForm(request.POST, instance=teacher)

        if form.is_valid():
            form.save()
            return redirect('teacher')
        else:
            print(form.errors)
    context={
        'form': form
    }
    return render(request, 'teacher/update.html',context)

# delete the teacher from the list
def teacher_delete(request, id):
    teacher = Teacher.objects.filter(id=id).delete()
    return redirect('teacher')


from teacher.forms import GradeForm
from teacher.models import Grade


def grade_list(request):
    grades = Grade.objects.all()
    context = {
        'grades': grades
    }
    return render(request, 'grade/index.html',context)


def grade_create(request):
    form = GradeForm()

    if request.method == "POST":
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grade')
        else:
            print(form.errors)
        
    context = {
        'form': form
    }

    return render(request, 'grade/create.html',context)


def grade_update(request, id):
    grade = Grade.objects.get(id=id)
    form = GradeForm(instance=grade)

    if request.method == "POST":
        form = GradeForm(request.POST, instance=grade)
        if form.is_valid():
            form.save()
            return redirect('grade')
        else:
            print(form.errors)

    context = {
        'form': form
    }

    return render(request, 'grade/update.html',context)


def grade_delete(request, id):
    grade = Grade.objects.get(id=id)
    grade.delete()
    return redirect('grade')