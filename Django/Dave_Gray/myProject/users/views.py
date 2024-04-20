from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def register(request):
    print("REGISTER")
    if request.method == "POST":        # POST -> FORM WAS SUBMITED    
        form = UserCreationForm(request.POST)       # load filled form
        if form.is_valid():
            login(request,form.save())              # Save User + log in
            return redirect("posts:list")           # redirect to Posts List (ReverseMatch)
        else:     
            print("INVALID REGISTER")
    else:                               #  GET ->  FORM IS REQUESTED                       
        form = UserCreationForm( )                  # Show empty form for Submition 
        print("REGISTER IS REQUESTED")
    return render( request, 'users/register.html',  # SHOW ANY FORM
                   { "form": form } )

#######################################################################
#######################################################################

def login_view(request):
    print("LOGIN")
    if request.method == "POST":         # POST -> FORM WAS SUBMITED    
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            print("VALID LOGIN")
            login(request, form.get_user())     # log in from form data
            if 'next' in request.POST:
                print("LOGIN URL NEXT QUERRY")
                return redirect(request.POST.get('next')) # redirect NewPost
            return redirect("posts:list")       # redirect to Posts List (ReverseMatch)
        else:
            print("INVALID LOGIN")
    else:                               #  GET ->  FORM IS REQUESTED 
        print("LOG IS REQUIRED ")
        form = AuthenticationForm()             # Show empty form for Submition 
    return render( request, 'users/login.html', # SHOW ANY FORM
                { "form": form } )

def logout_view(request):
    print("LOGOUT")
    if request.method == "POST":         # POST -> FORM WAS SUBMITED
        logout(request)                     # logout
        return redirect("posts:list")       # redirect to Posts List (ReverseMatch)
        


# Fotrm woth validatiom
''' user registrated must be new one
if not "USER ALLREDY EXIST"
'''
