from django.shortcuts import render ,HttpResponse
from django.http      import HttpResponseForbidden
from home.models      import Task
import datetime

# Create your views here.
def home (request) :
    context = {'success': False }
    if request.method == 'POST':
        print("This is POST method")
        
        if 'csrfmiddlewaretoken' not in request.POST:       # Check  CSRF token is included in request
            return HttpResponseForbidden('CSRF token missing')  # Return Forbidden response
        title  = request.POST.get('title', '')  # var = html
        desc   = request.POST.get('desc',  '')  
        time   = datetime.datetime.now()
        
        print(title, desc)
        instance = Task( taskTitle = title, taskDesc = desc, time = time)
        instance.save() # saved to DATABASE
        print("saved to DATABASE")
        context = {'success': True }

    return render(request, "index.html", context)

def tasks (request) :
    return render(request,"tasks.html")