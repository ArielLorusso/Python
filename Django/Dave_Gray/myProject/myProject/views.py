from django.http import HttpResponse
from django import views



def homepage(request):
    return HttpResponse("this is /home")

def about(request):
    return HttpResponse("this is /about")