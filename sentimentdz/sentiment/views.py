from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .apps import SentimentConfig
from django.http import JsonResponse
from rest_framework.views import APIView
def home(request):
   return HttpResponse('This is home')
   # return render(request,'sentimentdz\templates\home.html')








