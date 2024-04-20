from django import forms
from . import models

from PIL import Image

from .models import Post
from django.utils import timezone

class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title','body','slug','banner']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.user = user
    

    def clean_banner(self):     # clean_<fieldname>()  Django form method   called  "during form validation"

        banner = self.cleaned_data.get('banner')    # MAX_RESOLUTION 300 x 300
        if banner:                              
            img = Image.open(banner)
            width, height = img.size
            if width > 300 or height > 300:     
                raise forms.ValidationError("Image resolution must be less than 300x300 pixels.")
        return banner
    
    def clean(self):                                # MIN_TIME = 1 minute
        cleaned_data = super().clean()              
        user = self.user
        last_post = Post.objects.filter(author=user).order_by('-date').first()
        if last_post:
            time_difference = timezone.now() - last_post.date
            if time_difference.total_seconds() < 60:  # Limit to 60 seconds
                raise forms.ValidationError("You can only upload one post per minute.")
        return cleaned_data
        