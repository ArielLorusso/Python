from django.db import models
from django.contrib.auth.models import User

# https://docs.djangoproject.com/en/5.0/ref/models/fields/

class Post(models.Model):
    title = models.CharField(max_length=75) # string field, for small- to large-sized
    body  = models.TextField()              # default form widget for this field = Textarea.
    slug  = models.SlugField()              # label contais only letters, numbers, underscores or hyphens. Used in URLs.
    date  = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default='fallback.png', blank=True)
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    # SQL Tables :
    #  POSTS --->  USERS        If user is deleted all its Post will also delete 
    #   many  to   1   Relationship

    def __str__(self) -> str:
        return self.title