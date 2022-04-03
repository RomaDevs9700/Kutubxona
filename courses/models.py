from django.db import models

class Speciality(models.Model):
    name = models.CharField(max_length=100)
    code = models.IntegerField()
    start_date = models.DateField()
    is_active = models.BooleanField()

    def __str__(self):
        return self.name


class Teacher(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    degree = models.CharField(max_length=50)
    gender = models.BooleanField()
    phone = models.SmallIntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Subject(models.Model):
    name = models.CharField(max_length=200)
    specialities = models.ManyToManyField(Speciality)
    teachers = models.ManyToManyField(Teacher)
    number_of_pages = models.SmallIntegerField()

    def __str__(self):
        return self.name
