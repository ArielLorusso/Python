from django.shortcuts import render ,HttpResponse

# Create your views here.
def home(request):
    return render(request, 'index.html')

def blog(request):
    return render(request, 'blogpost.html')

def blogpost(request,slug):
    return render(request, 'blogpost.html')
    return HttpResponse(f"this is blogpost/{slug}")

def contact(request):
    return render(request, 'contact.html')

def search(request):
    return render(request, 'search.html')
