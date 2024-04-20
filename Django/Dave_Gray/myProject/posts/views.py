from django.shortcuts import render
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
    form = forms.CreatePost()
    return render( request, 'posts/post_new.html',{"form",form})
