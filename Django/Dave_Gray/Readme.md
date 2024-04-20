https://www.youtube.com/playlist?list=PL0Zuz27SZ-6NamGNr7dEqzNFEcZ_FAUVX
https://github.com/gitdagray/django-course/

# OVERVIEW
PROJECT & APP :
```sh
django-admin startproject NAME    # creates manage.py & in a Project direcory : settings.py urls.py views.py 
django-admin startapp     NAME    # creates APP dierectory  ( does't make  urls.py )
python3 manage.py runserver       # 127.0.0.1:8000
python3 manage.py createsuperuser # ADMIN
python3 manage.py shell           # Django shell
```
URLS :
```py
#  APP_URL      path('APP/', include('APP.urls' )), 
#  VIEW_URL     path('URL'          , views.function,  name='view_name'),
#  VIEW_URL     path('<slug:slug>'  , views.function , name='view_name'),
                # <Path_Converte:Parameter>'  Parameter= Row of SQL table by MODELS & ORM 
#  TEMPLATE     {% url  'app_name:view_name'  param1=value1  param2=value2  %}
#  REDIRECT     reverse('app_name:view_name' )
```
SETTINGS :
```py
# INSTALLED_APPS = [ "APP1", "APP2", ... etc ]
# TEMPLATES  = [   { "DIRS": ['templates'], ...  }   ]
# STATIC_URL = "static/"   STATICFILES_DIRS = [ os.path.join(BASE_DIR,'static')  ]
# MEDIA_URL  = 'media/'          MEDIA_ROOT =   os.path.join(BASE_DIR, 'media' )
```
MODELS:
```py 
        models.py:  # class Post(models.Model):
        admin.py :  # admin.site.register( MODEL )
        makemigrations: # python3 manage.py makemigrations 
        migrate :       # python3 manage.py migrate 
        superuser:      # python3 manage.py createsuperuser
        SQL_shell:      # python3 manage.py shell
        instance.save()
objects.create()
objects.get()
objects.update()
objects.delete()
objects.filter()
objects.count()
objects.last()
objects.first()
objects.union()
objects.intersection()
```
TEMPLATES:
```py
{{ variable }}       # passed as context in views.py
{% static 'FILE' %}  # file mist be inside static directory
{% csrf_token    %}  # forms require token
{% url  <path>   %}  # <a href='USE IT HERE'>
{% extends "base.html" %}
{% block <title>  %}            CONTENT             {% endblock %}
{% for <elem> in <context> %}   {{ elem.param }}    {% endfor %}
{% if  <elem =! 0> %}           HTML                {% endif %}
```
VIEWS:
```py
def view_function (request):
    instance = MODEL.objects.all().order_by("-FIELD")     # Reverse order by specified FIELD 
    context  = { "MODEL": instance }
    return render( request, 'APP/file.html',  context )   # full path = APP/Template/APP/file.html
    return redirect("APP:view_name")                      # using ReverseMatch
    return HttpResponse("AS HTML CONTENT" )               # for debugging purposes
```

#  VIDEO 1/12               Introduction and Beginners

## UPDATE TO DJANGO 5


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
## START PROJECT
```sh
django-admin startproject myProject
python3 manage.py runserver
> Django version 5.0.4, using settings 'myProject.settings'
> Starting development server at http://127.0.0.1:8000/
> [07/Apr/2024 00:23:59] "GET / HTTP/1.1" 200 292
```
## ROURING                  10:00
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
## TEMPLATES                15:00
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
## DJANGO TEPMLATE          13:00
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

{% clock title%}        <!-- HEAD tab title -->
    Home
{% endblock %}

{% clock content%}      <!--  BODY content -->
    <h1>Home</h1>
    <p> checkout my   <a href="/about">About</a>     page  </p>
{% endblock %}

```
## POST TEMPLATE            20:00
### Dave_Gray/ myProject/ posts/ templates/ posts/ post_page.html
```html
{% extends 'layout.html' %}

{% block title %}
    Posts List
{% endblock %}

{% block content %}
    <h1>Posts List</h1>
{% endblock %}
```
do the samt to  myProject/ templates/ about.html


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
## SHOW DATA IN TEPLATE :   11:30
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

## {% URL %}  URL REVERSING 
### Dave_Gray/ myProject/ posts/ urls.py :
```py
    path( '' , views.posts_list, name='posts'),
```
We ADDED   name='posts' to name this URL endpoint :
http://127.0.0.1:8000/posts/  ->  name='posts'
### Dave_Gray/ myProject/ templates/ layout.html :
```py
<div>
    <a href="{% url 'posts' %}" > 🗞️ News </a>
</div>
```
## PATH CONVERTERS          5:00
https://docs.djangoproject.com/en/5.0/topics/http/urls/#path-converters

str  - Matches any non-empty string, excluding the path separator, '/'. This is the default if a converter isn’t included in the expression.
int  - Matches zero or any positive integer. Returns an int.
slug - Matches any slug string consisting of ASCII letters or numbers, plus the hyphen and underscore characters. For example, building-your-1st-django-site.
uuid - Matches a formatted UUID. To prevent multiple URLs from mapping to the same page, dashes must be included and letters must be lowercase. For example, 075194d3-6885-417e-a8a8-6c931e272f00. Returns a UUID instance.
path - Matches any non-empty string, including the path separator, '/'. This allows you to match against a complete URL path rather than a segment of a URL path as with str.

We use slug
### Dave_Gray/ myProject/ posts/ urls.py :
```py
    path  (  '<slug:slug>'      ,  views.post_page, name='page'),
# < path_converter : parameter >    view.function   URL_App_name for reversing
# this URL uses a Slug path_converter to search the parameter slug inside the posts_post (App_Model) SQL table created by ORM
```
## PATH REVERSING           10:00
### Dave_Gray/ myProject/ posts/ templates/ posts/ posts_list.html :
```py
<h2>
    <a href="{% url 'page' slug=post.slug %}">
        {{ post.title }}
    </a>
</h2>
```

## EMPTY DATA ERROR
### ERROR during template rendering :
In template /home/ariel/Desktop/Python/Django/Dave_Gray/myProject/posts/templates/posts/posts_list.html, error at line 12
Reverse for 'page' with keyword arguments '{'slug': ''}' not found. 1 pattern(s) tried: ['posts/(?P<slug>[-a-zA-Z0-9_]+)\\Z']
12	    <a href="{% url 'page' slug=post.slug %}">

### CAUSE : if Post element lacks a slug attribute or have it set to None, 
attempting to generate a URL using {% url 'page' slug=post.slug %} will fail, 
because Django won't be able to construct a valid URL 
## RENDER VIEW              14:20
### Dave_Gray/ myProject/ posts/ views.py :
```py
    post = Post.objects.get(slug=slug)
    context = { "post": post }
    return render(request, 'posts/post_page.html', context )
```

We select a sigle post by  .get(slug) method
but posts/post_page.html  does not exist... lets make it 

###  Dave_Gray/ myProject/ posts/ templates/ posts/ post_page.html
```py
{% extends "layout.html" %}

{% block title%}
    {{ post.title }}
{% endblock %}

{% block content%}
    <section>
        <h1>    {{ post.title }}   </h1>
        <p> {{ post.body  }} </p>    <br> <hr>
        <p> {{ post.date  }} </p>
    </section>
{% endblock %}

```
## SPAN for ACCESIBILITY 
We want it to read the emoji's content :
### Dave_Gray/ myProject/ templates/ layout.html :
```py
<a href="/" > 
    <span role="img" aria-label="Home"> 🏠 </span>     Home 
</a>  
```

# VIDEO 7/12                Upload & Display Images

## MEDIA SETTINGS :
### Dave_Gray/ myProject/ myProject/ settings.py :
```py
MEDIA_URL = 'media/'                            # name for generated folder
MEDIA_ROOT = os.path.join(BASE_DIR, 'media' )   # absolute path
```
## MEDIA STATIC URL :
### Dave_Gray/ myProject/ myProject/ urls.py :
```py
from django.conf.urls.static import static
from django.conf import settings

urlpatterns += static(settings.MEDIA_URL ,
                      document_root=settings.MEDIA_ROOT)
```
## add BANNER to POST MODEL  :
### Dave_Gray/ myProject/ posts/ models.py:
```py
    banner = models.ImageField( default='fallback.png' , blank=True )
```
## MAKEMIGRATIONS & MIGRATE  :
```sh
cd myProject/
python3 manage.py makemigrations
> Migrations for 'posts':
>   posts/migrations/0002_post_banner.py
>     - Add field banner to post
python3 manage.py migrate
> Operations to perform:
>   Apply all migrations: admin, auth, contenttypes, posts, sessions
> Running migrations:
>   Applying posts.0002_post_banner... OK
```
## Log as Admin & UPLOAD IMAGES
```sh
python3 manage.py runserver
> Starting development server at http://127.0.0.1:8000/
```
http://127.0.0.1:8000/admin/posts/post/  -> upload images 

Title:      My 2nd post
Body:       This is trash just to complete the data and in not being empty
slug:       secod-post
Banner:
    Currently:  neofetch.jpg    ☐ Clear
    Change:     [CHOOSE FILE]       <==== Upload
    No file chosen
## add IMAGES to TEMPLATES  
###  post_page.html   &    post_list.html :
```html
    <img
        class="banner" 
        src="{{ post.banner.url }}" 
        alt="{{ post.title }}" >
```
## STYLE IMAGE FULLSCREEN
### Dave_Gray/ myProject/ static/ css/ style.css :
```css
.banner {
    display: block;
    width: 100%;
    max-width: 800px;
}
```

# VIDEO 8/12                Challenge & Solution

## ASIGNMENT :              0:42

1) Make a User App to the project
2) Create Template : register.html
3) Rout the endpoint to :  127.0.01:8000/users/register
4) 
## SOULUTION :              2:30
### 1 APP & URL
   * (A)  CREATE APP in console :
```sh
    python3 manage.py startapp users
```
   * (B)  Register the APP  settings.py :
```py
    INSTALLED_APPS = [
        "users",
        "posts", ... ]
```  
   * (C)  ROUT APP in myProject/ urls.py :
```py
    path('users/', include('users.urls' )), # Project.APP.view
``` 
### 2 TEMPLATE
   * (A)  Create folder Templates/users inside Users
   * (B)  Create register.html in  Templates/users/register.html:
```html
    {% extends "layout.html" %}

    {% block title%}
        Users
    {% endblock %}

    {% block content%}
        <h1> Users </h1>
        <p> checkout    <a href="/">Home</a>     page  </p>
    {% endblock %}
```
### 3 VIEW
   * (A)  CREATE VIEW users() in myProject/ users/ views.py :
```py
from django.shortcuts import render

# Create your views here.
def users(request):
    context = None
    return render(request, 'users/register.html', context )
```
   * (B)  CREATE URLS & ROUT VIEW users() to myProject/ users/ urls.py :
```py
from django.urls import path
from . import views 

app_name = 'users'      # name for URL ReverseMatch

urlpatterns = [
    path('register/'     , views.register, name='register'),
#  <path converter: parameter>     view             name
]
```



# VIDEO 9/12                User Registration

## DJANGO USER FORM in VIEWS        1:30
### Dave_Gray/ myProject/ users/ views.py :
```py
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def register(request):
    form = UserCreationForm( )
    return render( request, 'users/register.html',
                   { "form": form } )
```                         
## DJANGO USER FORM in TEMPLATE     3:10
### Dave_Gray/ myProject/ users/ templates/ users/ register.html :
```py
{% block content%}
    <h1> Users </h1>
    <p> checkout    <a href="/">Home</a>     page  </p>
    <form  action="/users/register/" method="post" 
           class="form-with-validation" > 
        {% csrf_token %}
        {{ form }} 
        <button type="submit" > Submit </button> 
    </form>
{% endblock %}
```
## CONDITIONAL LOGIC                7:50 
### USERS VIEWS
```py
def register(request):
    if request.method == "POST":  # POST -> FORM WAS SUBMITED    
        form = UserCreationForm(request.POST)   # load filled form
        if form.is_valid():
            form.save()                         # Save User
            return redirect("posts:list")           # redirect to Post List (ReverseMatch)
        else:     # redirect("APP:VIEW")
            print("INVALID FORM")
    else:                       #  GET ->  FORM IS REQUESTED                       
        form = UserCreationForm( )              # Show empty form for Submition 
        print("FORM IS REQUESTED")
    return render( request, 'users/register.html', # SHOW ANY FORM
                   { "form": form } )
```
## CHANGE & FIX VIWE NAMES 
### CHANGE USER URLS
in CONDITIONAL LOGIC we redirected...   redirect("posts:list")
this ReverseSearch name does not exist couse i forgot this line
```py
app_name = 'posts'      # ADD APP NAME  (I FORGOT)
urlpatterns = [
    path(''                 , views.posts_list, name='list'), ]
```
### FIX TEMPLATES

```py
            <a href="{% url 'posts' %}" > 
            #  layout.html         CHANGED AS FOLLOW
            <a href="{% url 'posts:list' %}" >      # APP:VIEW

            <a href="{% url 'page'          slug=post.slug %}">
            #  posts_list.html  :  CHANGED AS FOLLOW
            <a href="{% url 'posts:page'    slug=post.slug %}">
```
## UPDATE NAVBAR                    14:00
###
```py
            <a href="{% url 'posts:list' %}" title="Log in">  
                <span role="img" aria-label="log in"> 🪪 </span>    Log in
            </a>
```


# VIDEO 10/12               Login Form  &  User Authentication
## ADD REGISTER IN NAVBAR           1:50
```py
            <a href="{% url 'users:register' %}" title="Log in">  
                <span role="img" aria-label="log in"> 🔑 </span>    Log in
            </a>
```
## ADD REGISTER TO URLS             3:30
```py
    path('login/'       , views.login_view, name='login'),
```
## ADD REGISTER VIEWS               4:40
```py
def register(request):
    print("REGISTER")
    if request.method == "POST":        # POST -> FORM WAS SUBMITED    
        form = UserCreationForm(request.POST)       # load filled form
        if form.is_valid():
            login(request,form.save())              # Save User
            return redirect("posts:list")           # redirect to Post List (ReverseMatch)
        else:     
            print("INVALID REGISTER")
    else:                               #  GET ->  FORM IS REQUESTED                       
        form = UserCreationForm( )                  # Show empty form for Submition 
        print("REGISTER IS REQUESTED")
    return render( request, 'users/register.html',  # SHOW ANY FORM
                   { "form": form } )
```
## ADD LOGIN TEMPLATE FORM          7:40
```py
{% extends "layout.html" %}

{% block title%}
    User Log in
{% endblock %}

{% block content%}
    <h1> User Log in </h1>
    <p> checkout    <a href="/">Home</a>     page  </p>
    <form  action="/users/login/" method="post" 
           class="form-with-validation" > 
        {% csrf_token %}
        {{ form }} 
        <button type="submit" > Submit </button> 
    </form>
{% endblock %}
```
## ADD LOGIN VIEWS                  12:30
```py
from django.contrib.auth import login

def login_view(request):
    print("LOGIN")
    if request.method == "POST":         # POST -> FORM WAS SUBMITED    
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())     # log in from form data
            print("VALID LOG")
            return redirect("posts:list")       # redirect to Posts List (ReverseMatch)
        else:
            print("INVALID LOGIN")
    else:                               #  GET ->  FORM IS REQUESTED 
        form = AuthenticationForm()             # Show empty form for Submition 
        print("LOG IS REQUIRED ")
    return render( request, 'users/login.html', # SHOW ANY FORM
                { "form": form } )
```

# VIDEO 11/12               User Authorization

## LOGOUT URL               1:20         
```py
    path('logout/'    , views.logout_view, name='logout'),
```
## LOGOUT VIEW              2:00
```py
from django.contrib.auth import login, logout

def logout_view(request):
    print("LOGIN")
    if request.method == "POST":         # POST -> FORM WAS SUBMITED
        logout(request)                     # logout
        return redirect("posts:list")       # redirect to Posts List (ReverseMatch)
        
```
## LOGOUT Layout.html       4:20
```html
        <form class="logout" action="{% url 'users:logout'%}" method="post">
            {% csrf_token %}
            <button class="logout-button" aria-label="User Logout" title="User Logout"> 
                <a>🔒 Log out </a>
            </button>
        </form>
```
## NEWPOST URL              8:00
```py
    path('new-post/'        , views.post_new ,  name='new-post'),   
```
## NEWPOST VIEW             9:08
```py
@login_required(login_url="/users/login")   # THIS REDIRECTS TO LOG IN
def post_new (request):                     # contains a next query
    return render( request, 'posts/post_new.html')
```
`@login_required`    decorator :
typically `redirects` including a `query` parameter named `next` in the URL. 
This parameter contains the URL the user originally requested 
before being redirected to the login page.

in this case :
        REDURECS TO :                        QUERY:
        http://127.0.0.1:8000/users/login/   ?next=/posts/new-post/
## NEWPOST TEMPLATE         10:25
```py
{% extends "layout.html" %}

{% block title%}
    New Post
    {% endblock %}
    
    {% block content%}
    <section>
        <h1> New Post</h1>
    </section>
{% endblock %}

```
## NEWPOST add to LAYOUT    12:00
```py
    <a href="{% url 'posts:new-post' %}" title="New Post">  
        <span role="img" aria-label="New Post"> 🆕 </span>    New Post
    </a>
```
## RETUNR AFTER LOGIN       16:20

`<input type="hidden" name="next" value="{{ request.GET.next }}">`
is responsable for returning to New post after login
Will get used in `login_view()` to redirect back :
```py
        if 'next' in request.POST:
            return redirect(request.POST.get('next'))
```
this line is the responsable for the URL
127.0.0.1:8000/users/login/?next=/posts/new-post/
 to contain the querry : `next=/posts/new-post/`

This happen whe we enter   `new-post` without `log in` 
    http://127.0.0.1:8000/posts/new-post/
    will get redirected to :
    http://127.0.0.1:8000/users/login/?next=/posts/new-post/
    in order to it return automaticaly once we log

This behaviour would not be used much once we make the Nav-Bar interactive

### ADD NEXT TO LOGIN TEMPLATE 
```html
{% extends "layout.html" %}

{% block title%}
    User Log in
{% endblock %}

{% block content %}
    <h1> User Log in </h1>
    <p> checkout    <a href="/">Home</a>     page  </p>
    <form  action="/users/login/" method="post" 
           class="form-with-validation" > 
        {% csrf_token %}
        {{ form }}
        {% if request.GET.next %}
        <input type="hidden" name="next" value="{{ request.GET.next }}">
        {% endif %}
        <button type="submit" > Submit </button> 
    </form>
{% endblock %}
```
### ADD NEXT TO LOGIN_VIEW()
```py
def login_view(request):
    print("LOGIN")
    if request.method == "POST":         # POST -> FORM WAS SUBMITED    
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            print("VALID LOGIN")
            login(request, form.get_user())     # log in from form data
            if 'next' in request.POST:
                print("LOGIN URL NEXT QUERRY")
                return redirect(request.POST.get('next')) # redirect NewPost
            return redirect("posts:list")       # redirect to Posts List (ReverseMatch)
        else:
            print("INVALID LOGIN")
    else:                               #  GET ->  FORM IS REQUESTED 
        print("LOG IS REQUIRED ")
        form = AuthenticationForm()             # Show empty form for Submition 
    return render( request, 'users/login.html', # SHOW ANY FORM
                { "form": form } )
```
## INTERACTIVE NVAR LOGIC   20:46
```html
{% if user.is_authenticated %}
                <a href="{% url 'posts:new-post' %}" title="New Post" class="nav-button">  
                    <span role="img" aria-label="New Post"> 🆕 </span>    New Post
                </a>

                
                <form  action="{% url 'users:logout'%}" method="post" >
                    {% csrf_token %}
                    <button type="submit" class="nav-button" id="nav-logout" aria-label="User Logout" 
                    title="User Logout">🔒 Log out</button>
                </form>

            {% else %} <!-- NOT LOGGED IN-->
                <a href="{% url 'users:register' %}" class="nav-button" title="Register">  
                    <span role="img"  aria-label="Register">
                    🪪 </span>    Register
                </a>
                <a href="{% url 'users:login' %}" class="nav-button" title="Log in">  
                    <span role="img"  aria-label="log in">
                    🔑 </span>     Log in
                </a>
            {% endif %}
```

# VIDEO 12/12               Django Forms

## CUSTOM FORM NEW POST     
