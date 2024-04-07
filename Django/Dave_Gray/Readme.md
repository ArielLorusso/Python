https://www.youtube.com/playlist?list=PL0Zuz27SZ-6NamGNr7dEqzNFEcZ_FAUVX

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

#  VIDEO 2/12               App & Templates

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
###
###
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
###