from django.shortcuts import render ,HttpResponse
from blog.models import Blog

def home(request):
    return render(request, 'index.html')

def blog(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs }
    return render(request, 'bloghome.html', context)

def blogpost(request,slug):
    return render(request, 'blogpost.html')
    return HttpResponse(f"this is blogpost/{slug}")

def contact(request):
    return render(request, 'contact.html')

def search(request):
    return render(request, 'search.html')
