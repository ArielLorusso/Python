from django.shortcuts import render ,HttpResponse
from blog.models import Blog

def home(request):
    return render(request, 'index.html')

def blog(request):
    blogs = Blog.objects.all()   # Blogs are objects retreved by ORM
    context = {'blogs': blogs }  # context must be a dictionary  key-value
    return render(request, 'bloghome.html', context) 

def blogpost(request,slug):
    blog = Blog.objects.filter(slug=slug).first()
    context = {'blog': blog }
    return render(request, 'blogpost.html',context)


def contact(request):
    return render(request, 'contact.html')

def search(request):
    return render(request, 'search.html')
