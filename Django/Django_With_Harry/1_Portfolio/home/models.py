from django.db import models


class Contact (models.Model):
    name  = models.CharField  (max_length=30)
    email = models.EmailField ()
    phone = models.CharField  (max_length=30)
    desc  = models.TextField  ()

    def __str__(self) -> str:           # shown in /admin 
        return self.name  + ' - ' + self.email      