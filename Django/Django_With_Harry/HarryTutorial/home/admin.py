from django.contrib import admin
from home.models import Contact


# Register your models here.
admin.site.register(Contact)  # to view from 8000/admin      : Contacts
                              # it's allways plural (extra s aded by Django)  