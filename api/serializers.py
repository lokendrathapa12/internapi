from attr import fields
from api.models import UserProfile,Task,Attendence
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id','user','role']
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','task_name','task_des','note','task_release_date','task_expire_date','assigned_to','status','marks']

class AttendenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendence
        fields = ['id','user','attend_report','date','userprofile']
