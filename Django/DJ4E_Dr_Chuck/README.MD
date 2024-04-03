

# MAKE IT WORK 

To use Django Samples we will need to create Migrations a superuser and runserver
Make sure to be in the Project directory
```sh
    $ python3 manage.py migrate

    $ python3 manage.py createsuperuser

    $ python3 manage.py runserver
```

We can now enter http://127.0.0.1:8000/ on browser and use the superuser we just created
