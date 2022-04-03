from django.contrib import admin
from.models import Speciality, Teacher, Subject

@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    search_fields = ('name', 'code',)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name',)
    list_filter = ('degree',)

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    search_fields = ('name', 'specialities', 'teachers',)
    autocomplete_fields = ('specialities', 'teachers',)



