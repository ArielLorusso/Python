from django.db import models

# Create your models here.
class Blog(models.Model):
    sno     = models.AutoField( primary_key=True )
    title   = models.CharField( max_length=200 )
    content = models.TextField()
    slug    = models.CharField( max_length=100 )
    time    = models.DateField( auto_now_add = True )

    def __str__(self) -> str:   # No need to migrate this change
        return self.title       # this changes ho we see blogs....  Blog.object -> title 