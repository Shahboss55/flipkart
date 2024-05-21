from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
#  path("",views.babu),
   path("",views.respon,name="home"),
   path("about/",views.aboutus,name="about"),
   path("contact/",views.Contact,name="contact"),
   path("services/",views.Services,name="service"),
   path("profiles/",views.Profile,name="profile"),
]