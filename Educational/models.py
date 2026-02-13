from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.IntegerField()
    location = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    religion = models.CharField(max_length=100)
    board = models.CharField(max_length=100)
    personal_pc = models.CharField(max_length=100)
    personal_phn = models.CharField(max_length=100)

class MCQ(models.Model):
    ques = models.CharField(max_length=200)
    opt_1 = models.CharField(max_length=120)
    opt_2 = models.CharField(max_length=120)
    opt_3 = models.CharField(max_length=120)
    opt_4 = models.CharField(max_length=120)
    ans = models.IntegerField()
    marks = models.IntegerField()
    subject = models.CharField(max_length=50)

class True_False(models.Model):
    ques = models.CharField(max_length=200)
    ans = models.IntegerField()
    marks = models.IntegerField()
    subject = models.CharField(max_length=50)

class LongQues(models.Model):
    ques = models.CharField(max_length=200)
    marks = models.IntegerField()
    subject = models.CharField(max_length=50)

class Courses(models.Model):
    Course_title = models.CharField(max_length=200)
    duration = models.IntegerField()
    price = models.FloatField()

class invoice(models.Model):
    client_name=models.CharField(max_length=100)