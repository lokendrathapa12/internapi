from atexit import register
from pkgutil import ImpImporter
from posixpath import basename
from urllib.parse import parse_qs
from django import views
from django.db import router
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.views import  ProfileView,TaskView,AttendenceView,TaskViewDetail
from rest_auth.views import (
   LoginView, LogoutView, UserDetailsView, PasswordChangeView)

router = DefaultRouter()
router.register(r'userprofileapi',ProfileView ,basename='userprofile')

urlpatterns = [
    path('',include(router.urls)),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('login/$', LoginView.as_view(), name='rest_login'),
    path('logout/$', LogoutView.as_view(), name='rest_logout'),
    path('taskpageapi/',TaskView.as_view(),name='task'),
    path('taskdetailpageapi/<int:pk>/',TaskViewDetail.as_view(),name='taskretrieve'),
    path('attendenceapi/',AttendenceView.as_view(),name='attend'),
]   