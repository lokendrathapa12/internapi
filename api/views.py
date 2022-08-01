from urllib import response
from django.shortcuts import render
from requests import delete, request
from api.models import Attendence, UserProfile,Task
from api.serializers import ProfileSerializer,TaskSerializer,AttendenceSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.http import Http404

# Create your views here.


class ProfileView(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer

class TaskView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request, format= None):
        task = Task.objects.all()
        serializer = TaskSerializer(task, many=True)
        return Response(serializer.data)

    def post(self,request,format= None):
        user = request.user
        current_user = UserProfile.objects.filter(user=user)[0]
        urrent_user = UserProfile.objects.filter(user=user)
        if current_user.role == 'S':
            serializer= TaskSerializer(data= request.data)
            if serializer.is_valid():
                serializer.save()
                return Response (serializer.data,status=status.HTTP_200_OK, data={'message':'upload successfully'})
            return Response(status = status.HTTP_400_BAD_REQUEST, data={'message':'not valid'})
        return Response(status = status.HTTP_400_BAD_REQUEST,data ={'message':'role should be Supervisor'})



class TaskViewDetail(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404
    def get(self,request,pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self,request, pk, format = None):
        user = request.user
        current_user = UserProfile.objects.filter(user=user)[0]  
        if current_user.role == 'S':
            task = self.get_object(pk)
            serializer = TaskSerializer(task, data = request.data)   
            if serializer.is_valid():
                serializer.save()
                return Response (serializer.data,status=status.HTTP_200_OK, data={'message':'upload successfully'})
            return Response(status = status.HTTP_400_BAD_REQUEST, data={'message':'not valid'})
        return Response(status = status.HTTP_400_BAD_REQUEST,data ={'message':'role should be Supervisor'})

    def patch(self,request,pk,format=None):
        user = request.user
        currentt_user = UserProfile.objects.filter(user=user)[0]
        if currentt_user.role == 'S' and currentt_user.status == 'C':
            task = self.get_object(pk)
            serializer = TaskSerializer(task,request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK,data={'message':'Partially update succesfully !!'})
            return Response(status=status.HTTP_400_BAD_REQUEST,data={'message':'not valid'})
        return Response(status=status.HTTP_400_BAD_REQUEST,data={'message':'Role Should be Supervisor and status shoul be complete'})

    def delete(self,request,pk,format=None):
        user = request.user
        currentt_user = UserProfile.objects.filter(user=user)[0]
        if currentt_user.role == 'S':
            task = self.get_object(pk)
            task.delete()
            return Response(status=status.HTTP_200_OK,data={'message':'Delete Succesfully !!'})
        return Response(status = status.HTTP_400_BAD_REQUEST,data ={'message':'role should be Supervisor'})

class AttendenceView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
        attend = Attendence.objects.all()
        serializer = AttendenceSerializer(attend,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        user = request.user
        current_user = UserProfile.objects.filter(user=user)[0]
        print(current_user)
        if current_user.role == 'I':
            serializer = AttendenceSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK,data={'message':'your presantation upload succesfully'})
            return Response(status = status.HTTP_400_BAD_REQUEST, data={'message':'not valid'})
        return Response(status = status.HTTP_400_BAD_REQUEST,data ={'message':'role should be Supervisor'})
