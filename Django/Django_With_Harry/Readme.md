ProgrammingWithHarry :  Django Tutorials For Beginners         ( 2021  Django 3.1 ) https://endoflife.date/django
`https://www.youtube.com/watch?v=DR0Kbx1N1TU&list=PLK8cqdr55Tsv-D2HMdrnD32oOVBNvmxjr`

# Create project
# superuser
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

