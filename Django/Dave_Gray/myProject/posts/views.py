from django.shortcuts import render ,redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def posts_list (request):
    posts = Post.objects.all().order_by("-date")
    #context = { "posts": posts }
    return render( request, 'posts/posts_list.html', 
                   { "posts": posts } )

def post_page (request,slug):
    post = Post.objects.get(slug=slug)
    #context = { "post": post }
    return render( request, 'posts/post_page.html', 
                   { "post": post } )

@login_required(login_url="/users/login")   # THIS REDIRECTS TO LOG IN
def post_new (request):                     # contains a next query
    if request.method =='POST':
        form = forms.CreatePost(request.POST, request.FILES)    # FILLED FORM
        if form.is_valid() :
            newpost = form.save(commit=False) # NOT to database YET.  return an unsaved model
            #                   commit=False  Temporary model updated for manipulation 
            newpost.author = request.user
            newpost.save()  # ACTUALLY SAVE
            return redirect('posts:list')
        else:
            # Form validation failed, re-render the form with errors
            return render(request, 'posts/post_new.html', {'form': form})
    else:    
        form = forms.CreatePost(user=request.user)   # EMPTY FORM
        return render(request, 'posts/post_new.html', { 'form': form })
