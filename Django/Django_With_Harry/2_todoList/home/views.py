from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import render ,HttpResponse
from django.http      import HttpResponseForbidden
from home.models      import Task
import datetime

# Create your views here.
def home (request) :
    context = {'success': False, "name":"harry" }
    # https://docs.djangoproject.com/en/5.0/ref/request-response/#attributes-set-by-middleware
    if request.method == 'POST':
        print(request)          # <WSGIRequest: POST '/'>
        print(request.body)     # b'csrfmiddlewaretoken=0zEmyK1ahXjtrgPagJQQHc2MxEeGz3IDE2yTrlgm8uWKcas5DUm3JLrSYoGrOZzy&title=AAAAAAAAAAAAAAAAAAAAAAAAA&desc=BBBBBBBBBBBBBBBBBBBBBBBBBBBB'
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
        context.update({'success': True })

    return render(request, "index.html", context)

def tasks(request):
    all_tasks = Task.objects.all()
    context = {'tasks': all_tasks}
    return render(request, "tasks.html", context)

def edit_task(request, task_id):  # Define a new view function to handle editing tasks
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        # Handle form submission for editing task
        task_id = Task.objects.all()
        context = {'edit_mode ': True}
        # Update task details and save to database
        return redirect('tasks',context)  # Redirect after editing task

def delete_task(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id)
        task.delete()
        return redirect('tasks')  # Redirect after deleting task
    else:
        return HttpResponse.NotAllowed(['POST'])

{'Content-Length': '139', 
'Content-Type': 'application/x-www-form-urlencoded', 
'Host': '127.0.0.1:8000', 
'Connection': 'keep-alive', 
'Cache-Control': 'max-age=0', 
'Sec-Ch-Ua': '"Chromium";v="123", "Not:A-Brand";v="8"', 
'Sec-Ch-Ua-Mobile': '?0',
'Sec-Ch-Ua-Platform': '"Linux"',
'Upgrade-Insecure-Requests': '1',
'Origin': 'http://127.0.0.1:8000',
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-User': '?1', 
'Sec-Fetch-Dest': 'document', 
'Referer': 'http://127.0.0.1:8000/', 
'Accept-Encoding': 'gzip, deflate, br, zstd', 
'Accept-Language': 'en-US,en;q=0.9', 
'Cookie': 'firstName=PEPE; lastName=SPONGE; csrftoken=OD4H3Lpm1HNrV4N5xlGncJzgBUCVp615; sessionid=e1ea614io6w4froeyaffk3tmoqwd5lmg'
}