ProgrammingWithHarry :  Django Tutorials For Beginners 
( 2021  Django 3.1 )    https://endoflife.date/django
`https://www.youtube.com/watch?v=DR0Kbx1N1TU&list=PLK8cqdr55Tsv-D2HMdrnD32oOVBNvmxjr`

1_Pertfolio & 2_todoList are not valid project names 
I changed i manually for the sake of order sice I wont add any app to them


# Create project
```sh
$ django-admin startproject  < Project_Name >
```
this will create a folder with Project name in current direcory
```sh
$ django-admin startapp  < appname >
```
## runserver

```sh
$ python3 manage.py runserver
```

# superuser
```sh
$ python3 manage.py createsuperuser
```
# manage.py
# urls.py
# Views.py
```py
    print(request)           # <WSGIRequest: POST '/'>
    print(request.headers)   # {'Content-Length': '139', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': '127.0.0.1:8000', 'Connection': 'keep-alive', 'Cache-Control': 'max-age=0', 'Sec-Ch-Ua': '"Chromium";v="123", "Not:A-Brand";v="8"', 'Sec-Ch-Ua-Mobile': '?0', 'Sec-Ch-Ua-Platform': '"Linux"', 'Upgrade-Insecure-Requests': '1', 'Origin': 'http://127.0.0.1:8000', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-User': '?1', 'Sec-Fetch-Dest': 'document', 'Referer': 'http://127.0.0.1:8000/', 'Accept-Encoding': 'gzip, deflate, br, zstd', 'Accept-Language': 'en-US,en;q=0.9', 'Cookie': 'firstName=PEPE; lastName=SPONGE; csrftoken=OD4H3Lpm1HNrV4N5xlGncJzgBUCVp615; sessionid=e1ea614io6w4froeyaffk3tmoqwd5lmg'}
    print(request.body)      # b'csrfmiddlewaretoken=0zEmyK1ahXjtrgPagJQQHc2MxEeGz3IDE2yTrlgm8uWKcas5DUm3JLrSYoGrOZzy&title=AAAAAAAAAAAAAAAAAAAAAAAAA&desc=BBBBBBBBBBBBBBBBBBBBBBBBBBBB'
    print(request.GET)       # <QueryDict: {}>
    print(request.POST)      # <QueryDict: {'csrfmiddlewaretoken': ['P68Ryt5Oip6DDmMJNnjpXwKXnOHyV9k2tz2or4k09WJUogpEayPCZ593Oy9ja5bX'], 'title': ['this_is_task_title'], 'desc': ['this_is_task_description']}>
    print(request.FILES)     # <MultiValueDict: {}>
    print(request.META)      # {'SHELL': '/bin/bash', 'SESSION_MANAGER': 'local/ariel-All-Series:@/tmp/.ICE-unix/1686,unix/ariel-All-Series:/tmp/.ICE-unix/1686', 'QT_ACCESSIBILITY': '1', 'COLORTERM':
    print(request.encoding)  # None
    print(request.scheme)    # http
    print(request.__iter__())# <callable_iterator object at 0x7f43b9e6ace0>
    print(request.user)      # admin
    print(request.session)   # <django.contrib.sessions.backends.db.SessionStore object at 0x7f644ffb1ff0>
```
# Templates
```py
{% %}
{% %}
{% %}

{% for  element in structure %}
    {{element}}
    {{forloop.counter}}
{% endfor %}

```
# models
# http

# AUTENTICATION & AUTORUZATION
user autentuication : mail and password to prove who the user is 
user autorization   : what user is alowed to do by permission 
user models profile emails paswords

Django aut model can be costumized for extra functionality
there are lots of tools most developers dont use so thei dont come by default in the users table

storing HASHED PASSWORDS will protect us in case the table is stolen
we can use this secure password we no not posess to encript users data

## Password Complexity
https://www.password-depot.de/en/know-how/brute-force-attacks.htm#:~:text=When%20creating%20a%20password%2C%20the%20following%20characters,A%2DZ%20and%20a%2Dz)%20Special%20characters%20(32%20different).
we cant demand the user to :
enter more than 8 characters
Have at least 1 special character , Uppercase & Number
Resulting in  94 symbols = 26 LowCase + 26 UppCase + 10 Num + 32 special
(94^8) = 6 10^15 ...   compared  to 2 10^11  for just 26 leters

Althoug Bruteforce can create about 10^9 passwods per second
Aur server's hash & compare arent wil determinate the Brutforce speed

### Django hash methods
https://docs.djangoproject.com/en/5.0/topics/auth/passwords/

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.ScryptPasswordHasher",
]
to avlid brutforce we can limit the tryes user can do.

## Trottling of log in aptempts
we can far example cunt rhe ammont of loggin aptempts in last 3 minutes
if it reaches 3 we can block anyt further aptempt for 3 minutes
this will result in a maximun aptempt rate of 0.5 try/minute
we would need to meke a list of last aptempts
it could be a circular list of last 3 aptempts 

django does not have this by default

# Third party autentication
Google Facebook Outlook


hostdomain.extension/App/funct/slug?field1=value1&field2=value2#Headline2

slug = variable --> django : <type:name>
? : querry separator
& : key-value separator
% : replace unsafe character ' ' = %20
# : Fragment (jump to a page section)