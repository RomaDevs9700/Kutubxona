from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=512)
    author = models.CharField(max_length=512)
    count = models.IntegerField(default=1)

    class Meta:
        db_table = "books"

    def __str__(self):
        return f"{self.title} by {self.author}"


class User(models.Model):
    STUDENT = "student"
    TEACHER = "teacher"
    ROLES = (
        (STUDENT, "Student"),
        (TEACHER, "Teacher")
    )

    role = models.CharField(max_length=10, choices=ROLES) #student ot teacher
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Bookrecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="book_records")
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    took_on = models.DateField()
    returned_on = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"User: {self.user} Book: {self.book}"

    @property
    def is_returned(self):
        return self.returned_on is not None

