from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# def babu(request):
#     return HttpResponse("rahulshah")
def respon(request):
   return render(request,"bossapp/respon.html")
def aboutus(request):
   return render(request,"bossapp/aboutus.html")
def Contact(request):
   return render(request,"bossapp/contactus.html")
def Services(request):
   return render(request,"bossapp/services.html")
def Profile(request):
   return render(request,"bossapp/profile.html")


