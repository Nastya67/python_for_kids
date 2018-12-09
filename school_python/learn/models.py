from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    idTask = models.IntegerField(primary_key=True, auto_created=True)
    coins = models.IntegerField(default=1)
    text = models.CharField(max_length=1000)


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    coins = models.IntegerField(default=0)

    def groups(self):
        return Gruop.objects.filter(idTeacher=self.id)


class Gruop(models.Model):
    idGroup = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=15)
    idTeacher = models.ForeignKey(Teacher)

    def mean_coins(self):
        students = Student.objects.filter(idGroup=self.idGroup)
        if len(students) == 0:
            return 0
        return sum([x.coins for x in students])/len(students)

    def size(self):
        return len(Student.objects.filter(idGroup=self.idGroup))

    def students(self):
        return Student.objects.filter(idGroup=self.idGroup)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    coins = models.IntegerField(default=0)
    idGroup = models.ForeignKey(Gruop, to_field="idGroup")

    def groupmates(self):
        return Student.objects.filter(idGroup=self.group)

    def group(self):
        return Gruop.objects.get(idGroup=self.idGroup)

