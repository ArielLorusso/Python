from django.shortcuts import render

# Create your views here.
def register(request):
    # context = None
    return render(request, 'users/register.html' )