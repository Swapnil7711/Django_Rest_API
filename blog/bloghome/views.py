from django.shortcuts import render, HttpResponse, get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import AppUsers
from .serializers import usersSerializer

# Create your views here.

# def home(request):
#     return HttpResponse('hello world')


class AppUsersList(APIView):

    def get(self, request):

        AppUser = AppUsers.objects.all()

        serialser = usersSerializer(AppUser, many=True)

        return Response(serialser.data)


    def post(self,request):
        serializer = usersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
