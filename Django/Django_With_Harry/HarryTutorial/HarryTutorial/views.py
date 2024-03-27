from django.shortcuts import render , HttpResponse
from home.models import Contact

# Create your views here.
def home (request) :
    # return HttpResponse ("this is ABOUT ")
    context  = { 'name'  :'Ariel',
                 'course':'Django'}
    return render (request, "home2.html",context)

def about (request) :
    return render (request, "about.html")

def projects (request) :
    return render (request, "projects.html")

def contact (request) :
    if request.method=="POST":
        print("This is POST method")
        name  = request.POST.get('name', '')  # Use get() to avoid KeyError
        email = request.POST.get('email', '')  # Use get() to avoid KeyError
        phone = request.POST.get('phone', '')  # Use get() to avoid KeyError
        desc  = request.POST.get('desc', '')  # Use get() to avoid KeyError
        print(name, email, phone, desc)
        instance = Contact(  name = name,
                        email= email,
                        phone= phone,
                        desc = desc,)
        instance.save() # saved to DATABASE
        print("saved to DATABASE")
    return render (request, "contact.html")


# VIEW IS : render by browser
# in this case a string
# can also be an HTML oe template