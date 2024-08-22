from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .serializer import *
from rest_framework import generics
# Create your views here.






def index(request):



    return HttpResponse("HOME..")




class View(generics.ListCreateAPIView):
    queryset = Try_2.objects.all()
    serializer_class = Try_2Serializer