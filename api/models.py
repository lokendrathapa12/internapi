from wsgiref.simple_server import demo_app
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    User_Choice = (
        ('I','Intern'),
        ('S','Supervisor')
    )
    role = models.CharField(max_length=20,choices=User_Choice,default='Intern')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='profile')
    
    def __str__(self):
        return self.role


class Task(models.Model):
    Status_Choice = (
        ('C','Complete'),
        ('P','Pending')
    )
    task_name = models.CharField(max_length=100)
    task_des = models.TextField(max_length=1000)
    note = models.CharField(max_length=500)
    task_release_date = models.DateTimeField(auto_now_add=True)
    task_expire_date = models.DateTimeField(auto_now_add=False)
    assigned_to = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.CharField(max_length=20,choices=Status_Choice,default='Pending')
    marks = models.BigIntegerField()
    

   

class Attendence(models.Model):
    us = models.ForeignKey(User,on_delete=models.CASCADE)
    userprofile = models.ForeignKey(UserProfile,on_delete=models.CASCADE, default='')
    attend_report = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True)