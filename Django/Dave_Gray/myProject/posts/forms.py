from django import forms
from . import models
from . import forms

class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title','body','slug','banner']
