from django.db import models

# Create your models here.
# https://docs.djangoproject.com/en/5.0/ref/models/fields/

class Post(models.Model):
    title = models.CharField(max_length=75) # string field, for small- to large-sized
    body  = models.TextField()              # default form widget for this field = Textarea.
    slug  = models.SlugField()              # label contais only letters, numbers, underscores or hyphens. Used in URLs.
    date  = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title