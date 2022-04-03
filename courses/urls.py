from courses.views import courses_view
from django.urls import path
from .views import courses_view, speciality_list, speciality_create
from .views import teacher_list, teacher_create, teacher_edit
from .views import subject_list, subject_create, subject_detail

urlpatterns = [
    path("courses/", courses_view, name="courses-list"),
    path("courses/speciality/", speciality_list, name="speciality-list"),
    path("courses/speciality/create/", speciality_create, name="speciality-create"),
    path("courses/teacher/", teacher_list, name="teacher-list"),
    path("courses/teacher/create/", teacher_create, name="teacher-create"),
    path("courses/teacher/edit/<int:pk>/", teacher_edit, name="teacher-edit"),
    path("courses/subject/", subject_list, name="subject-list"),
    path("courses/subject/create/", subject_create, name="subject-create"),
    path("courses/subject/<int:pk>/", subject_detail, name="subject-detail"),
]






