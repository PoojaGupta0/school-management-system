from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50, verbose_name="student_name")


class Teacher(models.Model):
    name = models.CharField(max_length=50, verbose_name="teacher_name")


class TeachersOfStudent(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    is_stared = models.BooleanField(default=False)
