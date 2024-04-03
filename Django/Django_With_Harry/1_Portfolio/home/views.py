from django.shortcuts import render , HttpResponse
from home import models

# Create your views here.
def home (request) :
    a = "<pre>This is the 8000/home/  page \n"
    a +=     "if you put  8000/home " 
    a += " Browser will correct you</pre>"
    a += "Test"
    return HttpResponse (a)

def home1 (request) :
    a = "This is  8000/home/home1 \n"
    return HttpResponse (a)

def home2 (request) :
    a = "This is  8000/home/home2 \n"
    return HttpResponse (a)


# VIEW IS : render by browser
# in this case a string
# can also be an HTML oe template