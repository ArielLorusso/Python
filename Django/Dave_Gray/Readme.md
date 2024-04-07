https://www.youtube.com/playlist?list=PL0Zuz27SZ-6NamGNr7dEqzNFEcZ_FAUVX
https://github.com/gitdagray/django-course/
#  VIDEO 1/12               Introduction and Beginners

##  UPDATE TO DJANGO 5

```sh
cd Dave_Gray/
python3  --version
> Python 3.10.12
pip install --upgrade Django
# --upgrade in case we allredy have Django instaled

>  Downloading Django-5.0.4-py3-none-any.whl (8.2 MB)
>     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.2/8.2 MB 8.0 MB/s eta 0:00:00
>  Successfully installed Django-5.0.4
pip list | grep django
> django-crispy-forms      2.0
> django-extensions        3.2.3
> django-filter            23.2
> django-taggit            4.0.0
> djangorestframework      3.14.0
> social-auth-app-django   5.2.0
pip list | grep Django
> Django                   5.0.4
```
##  START PROJECT

```sh
django-admin startproject myProject
python3 manage.py runserver
> Django version 5.0.4, using settings 'myProject.settings'
> Starting development server at http://127.0.0.1:8000/
> [07/Apr/2024 00:23:59] "GET / HTTP/1.1" 200 292
```
##  ROURING                  10:00
###     Dave_Gray/ myProject/ url.py :
```py
from . import views 

path(''      , views.homepage),
path('about/', views.about ),
```
###     Dave_Gray/ myProject/ view.py :
```py
from django.http import HttpResponse

def homepage(request):
    return HttpResponse("this is /home")

def about(request):
    return HttpResponse("this is /about")
```
##  TEMPLATES                15:00
###     Dave_Gray/ myProject/ myProject/ settings.py : : 
```json
TEMPLATES = [
    {   "DIRS": ['templates'],          }   ]
```
###     Dave_Gray/ myProject/ view.py :
```py
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
```
###     Dave_Gray/ template/ home.html :
```html
<!DOCTYPE html>
<head>
    <title>Home</title>
</head>

<body>
    <h1>Home</h1>
    <p> checkout my   <a href="/about">About</a>     page   </p>
</body>
</html>
```
do the same to   about.html     just change  link to   href=""> home
## STATIC CSS STYLE          20:00
###     Dave_Gray/ static/ css/  style.css :
```css
/*  RESET  EVERITHING*/
* {
    margin : 0;
    padding: 0;
}

/*  SET  BODY H1 P elements*/
body {
    min-height: 100vh;
    display: grid;
    place-content: center;
    font-size: 3rem;
    background-color: #222;
    color: #FFF;
}

h1, p {
    text-align: center;
}
```
###     Dave_Gray/ myProject/ myProject/ settings.py : :
```py
import os
STATIC_URL = "static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static')
]
```
###     Dave_Gray/ template/  home.html :
```html
    {% load static %}
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
```
result : 
<!-- <link rel="stylesheet" href="/static/css/style.css">   -->
`{% load static %}` : loads the `/static` folder before `index.html`
can be anywhere before the resource is used...

do the same to about.html

```sh
    python3  manage.py  runserver
```
## STATIC JS  SCRIPT         25:00
### Dave_Gray/ static/ js/  main.css 
```js
console.log("this is JS  from  About page")
```
###     Dave_Gray/ template/ home.html :
```html
<script src="{% static "js/main.js" %}" defer> </script>
<!-- defer : load JS after the whole html is loaded -->
```

#  VIDEO 2/12               APP & Templates

## VS-Code Extension
Django              v1.15.0     Baptiste Darthenay
Material Icon Theme v4.34.0     Philipp Kief
## APP : posts              2:45
```sh
python3 manage.py startapp posts
```
### Dave_Gray/ myProject/ posts/ views.py :
```py
def posts_list (request):
    return render(request, '')
``` 
      
### Dave_Gray/ myProject/ myProject/ settings.py :
```py
# Application definition
INSTALLED_APPS = [
    'posts',
    ]
```
## CREATE A NAMESPACE       5:30
We follow the pattern :     APP/ templates/ APP/ 
### Dave_Gray/ myProject/ posts/ templates/ posts/ posts_list.html :
```html
        <title>Post List</title>
            <h1>Post List</h1>
```
### Fix Emmet in VS-code settings :
```json
    "emmet.includeLanguages": { "django-html": "html" }
```
### Dave_Gray/ myProject/ posts/ urls.py :
```py
urlpatterns = [
    path(''      , views.posts_list),   ]
```
### Dave_Gray/ myProject/ posts/ views.py :
```py
def posts_list (request):
    return render(request, 'posts/posts_list.html')
```
### Dave_Gray/ myProject/ myProject/ urls.py :
```py
    from django.urls import path, include
    path('posts/', include('posts.urls' )),
```
## OPEN IN BROWSER          
```sh
python3 manage.py runserver
>Starting development server at http://127.0.0.1:8000/
```
BROWSER -->  http://127.0.0.1:8000/posts/
## ADVANCED TEPMLATE        13:00
### Dave_Gray/ myProject/ templates/ layout.html :
```html
<!DOCTYPE html>
{% load static %}
<html lang="en">
<head>
    <title>
        {% block title%}
        Django app  <!--Default value -->
        {% ensblock %}
    </title>
    <link  href="{% static 'css/style.css' %}" rel="stylesheet"> 
    <script src="{% static "js/main.js" %}" defer> </script>
</head>
<body>
    <nav>
        <a href="/"     > 🏠 </a>
        <a href="/about"> ℹ️  </a>
        <a href="/news" > 🗞️ </a>
    </nav>
    <main>
        {% block content%}
        {% endblock %}
    </main>
</body>
</html>
```
### Dave_Gray/ myProject/ templates/ home.html :
```html
{% extends "layout.html" %}

{% clock title%}
    Home
{% endblock %}

{% clock content%}
    <h1>Home</h1>
    <p> checkout my   <a href="/about">About</a>     page  </p>
{% endblock %}

```

## POST TEMPLATE            20:00

# VIDEO 3/12                MODELS and Migrations

## POST models.py :

### Dave_Gray/ myProject/ posts/ models.py  4:50
```py 
# https://docs.djangoproject.com/en/5.0/ref/models/fields/
class Post(models.Model):
    title = models.CharField(max_length=75) # string field, for small- to large-sized
    body  = models.TextField()              # default form widget for this field = Textarea.
    slug  = models.SlugField()              # label contais only letters, numbers, underscores or hyphens. Used in URLs.
    date  = models.DateTimeField(auto_now_add=True)
```

## Unaplyed Builtin Migrations
```sh
python3 manage.py runserver
> "You have 18 unapplied migration(s). Your project may not work properly"
> "until apply migrations for  app(s):" # admin, auth, contenttypes, sessions.
> "To apply them Run : "                # python manage.py migrate 
```

## MIGRATIE

```sh
ariel  $ python3 manage.py migrate 
> Operations to perform:
>   Apply all migrations: admin, auth, contenttypes, sessions
> Running migrations:
>   Applying contenttypes.0001_initial... # OK
>   Applying auth.0001_initial... # OK
>   Applying admin.0001_initial... # OK ...........
```

## MAKEMIGRATIONS           7:30

```sh
python3 manage.py makemigrations 
> Migrations for 'posts':
>   posts/migrations/0001_initial.py
>     - Create model Post
```
This created files : `posts/ migrations/ 0001_initial.py`

## AUTOMATIC ID as PRIMARY KEY
```py
migrations.CreateModel(
    name="Post"
    "id",
            models.BigAutoField(
                auto_created=True,
                primary_key=True, .... ).... )
```
`Field id` has been `added by Django` 
Because every `SQL table` needs a `primary key`


# VIDEO 4/12                ORM Object Relational Mapping

## DJANO SHELL ORM
```sh
python3 manage.py shell
> Python 3.10.12  [GCC 11.4.0]
> IPython 8.12.0 -- Interactive Python.      Type '?' for help.
> In [1]: ┃ 
```


```py
In [1]: from posts.models import Post
In [2]: p = Post()
In [3]: p
Out[3]: <Post: Post object (None)>
In [4]: p.title = "My first post"
In [5]: p.save()
In [6]: Post.objects.all()
Out[6]: <QuerySet [     <Post: Post object (1)>     ]>
In [7]: exit()
```

## ADD METHOD TO MODEL  4:00

Seeing   <Post: Post object (1)>  does not show much information about content
we can change how Table elements are displayed adding a method to see title

```py
    def __str__(self) -> str:
        return self.title
```
This does not change the data... just how its displayed
so no need for Migrations


```py
In [1]: from posts.models import Post
In [2]: p = Post()
In [3]: p.title = "My 2nd post"
In [4]: p.save()
In [5]: Post.objects.all()
Out[5]: <QuerySet [     <Post: My first post>, 
                        <Post: My 2nd post>         ]>
```

# VIDEO 5/12                ADMIN

## CREATE SUPERUSER         2:40
```sh
python3 manage.py createsuperuser
> Username (leave blank to use 'ariel'): **********
> Email address:  
> Password: *****
> Password (again): *****
> This password is too short. It must contain at least 8 characters.
> Bypass password validation and create user anyway? [y/N]: y
> Superuser created successfully.
```
## CANT SEE POSTS
when we log in in we just se `USERS`   
http://127.0.0.1:8000/admin/auth/user/
We do `NOT` se any `Post table`

## REGISTER the MODEL       6:00

### Dave_Gray/myProject/posts/admin.py
```py
from . models import Post
admin.site.register(Post)
```
## SEE MODEL in TABLE       7:00
Now wem we log in we see `USERS` & `POSTS`     
http://127.0.0.1:8000/admin/auth/user/
http://127.0.0.1:8000/admin/posts/post/

we can edit the data in the table
http://127.0.0.1:8000/admin/posts/post/1/change/
In order to edit, every field must contain a value 

we can see the HTTP request generated 
```sh
[07/Apr/2024 20:53:05] "POST /admin/posts/post/1/change/ HTTP/1.1" 302 0
[07/Apr/2024 20:53:05] "GET  /admin/posts/post/          HTTP/1.1" 200 9128
[07/Apr/2024 20:53:05] "GET  /admin/jsi18n/              HTTP/1.1" 200 3342
```
300: HTTP_REDIRECT   200: HTTP_OK
9128 & 3342 Size of  Response Body
/post     HTML for user to interact with our web
/jsi18n   endpoint for Djangos  Internationalization and localization
witch adapts the web contents depending on the user location time & language
https://docs.djangoproject.com/en/5.0/topics/i18n/

## PASS DATA TO VIEWS :     9:00
### Dave_Gray/ myProject/ posts/ views.py:
```py
def posts_list (request):
    posts = Post.objects.all().order_by("-date")
    context = { "posts": posts }
    return render(request, 'posts/posts_list.html', context )
```
### Dave_Gray/ myProject/ posts/ templates/ posts/ posts_list.html :
```py
    <h1> Post List</h1>
    {% for post in posts %}
        <article class="post">
            <h2>{{ post.title }} </h2>
            <p> {{ post.date  }} </p>
            <p> {{ post.body  }} </p>
        </article>
        <br> <hr>
    {% endfor %}
```

# VIDEO 6/12                Pages, URLs & Slugs

