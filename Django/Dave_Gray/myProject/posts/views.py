from django.shortcuts import render
from .models import Post

# Create your views here.
def posts_list (request):
    posts = Post.objects.all().order_by("-date")
    context = { "posts": posts }
    return render(request, 'posts/posts_list.html', context )