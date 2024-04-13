from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    if request.method == "POST":  # POST -> FORM WAS SUBMITED    
        form = UserCreationForm(request.POST)   # load filled form
        if form.is_valid():
            form.save()                         # Save User
            return redirect("posts:list")           # redirect to Post List (ReverseMatch)
        else:     # redirect("APP:VIEW")
            print("INVALID FORM")
    else:                       #  GET ->  FORM IS REQUESTED                       
        form = UserCreationForm( )              # Show empty form for Submition 
        print("FORM IS REQUESTED")
    return render( request, 'users/register.html', # SHOW ANY FORM
                   { "form": form } )


# Fotrm woth validatiom
''' user registrated must be new one
if not "USER ALLREDY EXIST"
'''