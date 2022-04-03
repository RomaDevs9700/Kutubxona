from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Speciality, Teacher, Subject
from .forms import SpecialityForm, SubjectForm, TeacherForm


def courses_view(request):
    name = request.GET.get("name", "Django")
    return HttpResponse(f"""
    <h1 style="color: green"> Hello {name} </h1>
    """)


def speciality_list(request):
    speciality = Speciality.objects.all()
    if len(speciality) == 0:
        speciality = "0"
    return render(request, "courses/speciality.html", {
            "speciality": speciality
        })

def speciality_create(request):
    if request.method == "GET":
        form = SpecialityForm()
    else:
        form = SpecialityForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Speciality.objects.create(
                name = data["name"],
                code = data["code"],
                start_date = data["start_date"],
                is_active = data["is_active"],
            )
            return redirect("speciality-list")
    return render(request, 'courses/speciality_create.html', {
        "form": form,
    } )


def teacher_list(request):
    search = request.GET.get("search")
    if search is None:
        teachers = Teacher.objects.all()
        return render(request, 'courses/teacher.html', {
            "teachers": teachers
        })
    else:
        teachers = Teacher.objects.filter(first_name__contains=search)
        if len(teachers) == 0:
            teachers = "0"
        return render(request, 'courses/teacher.html', {
            "teachers": teachers
        })

def teacher_create(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher-list')
    else:
        form = TeacherForm()
    return render(request, 'courses/teacher_create.html', {
        "form": form,
    } )


def teacher_edit(request, pk=None):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == "POST":
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher-list')
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'courses/teacher_edit.html', {
        "form": form,
        "teacher": teacher,
    } )


def subject_list(request):
    subjects = Subject.objects.all()
    if len(subjects) == 0:
        subjects = "0"
    return render(request, 'courses/subject.html', {
        "subjects": subjects
    })

def subject_create(request):
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subject-list')
    else:
        form = SubjectForm()
    return render(request, 'courses/subject_create.html', {
        "form": form,
    } )

def subject_detail(request, pk):
    subject = Subject.objects.get(pk = pk)
    return  render(request, 'courses/subject_detail.html', {
        "subject": subject,
    })


