from django.contrib import admin
from django.urls import path, include

from home import views # IMPERT VIEW OF USED APPS

urlpatterns = [
    path( "",        views.home, name='testt'   ),
    path( "home1/",  views.home1, name='homee'   ),
    path( "home2/",  views.home2, name='homee'   ),


]