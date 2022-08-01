from django.contrib import admin
from api.models import UserProfile,Task,Attendence
# Register your models here.
@admin.register(UserProfile)
class ProfileAdminModel(admin.ModelAdmin):
    list_display = ['id','user','role']

@admin.register(Task)
class TaskAdminModel(admin.ModelAdmin):
    list_display = ['id','task_name','task_des','note','task_release_date','task_expire_date','assigned_to','status','marks']

@admin.register(Attendence)
class AttendenceAdminModel(admin.ModelAdmin):
    list_display = ['id','us','attend_report','date','userprofile']
