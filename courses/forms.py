from django import forms
from django.forms import Form, ModelForm, fields
from .models import Speciality, Subject, Teacher

class SpecialityForm(forms.Form):
    name = forms.CharField(max_length=200)
    code = forms.IntegerField(min_value=1)
    start_date = forms.DateField()
    is_active = forms.BooleanField()


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'degree', 'gender', 'phone']
        

class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'specialities', 'teachers', 'number_of_pages'] 
