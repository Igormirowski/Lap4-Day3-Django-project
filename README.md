# LAP 4 Day 3 Django Project

[Django website step by step](https://www.djangoproject.com/start/)

### setup 
- `pip install pipenv `
- `pipenv shell `
- `pipenv install django`
- `django-admin startproject shelter` (name of project = shelter)

### Run server: 
- cd into shelter 
- `python manage.py runserver` --> localhost 8000

### PROJECT APP: 
- `python manage.py startapp adoption`
- add .gitignore 
- connect app to project: settings.py add to INSTALLED_APPS name of app(adoption)
- urls.py add path(adoption) and import include 

- create usrls.py in adoption(app name) folder and add stuff inside 
```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="adoption-home")
]
```
- add to views in adooption stuff
- `python manage.py runserver` see server 8000/adoptions 

- add about/ path in views
- add stuff to views.py (about) check 8000/adoption/about

- more path, dogs, show -> create new in views.py
- add doggos database
- see `http://localhost:8000/adoption/dogs and http://localhost:8000/adoption/dogs/1`

### templates
- create template/adoption/layout.html in adoption 
- connect layout/html to views.py:
 -  use `render` and change all functions in views.py and add all html files in adoption next to layout (home,about,dogs,show)
 - `home.html` add block and content
 - same with about and the rest



# DATABASE

- add stuff to models.py
- `python manage.py makemigrations adoption`  (models.py converted to sth understandable)
- `python manage.py migrate` run migration
- `python manage.py createsuperuser` igor igor@exampl.com igor12345  --> Created user in DJANGO
- `python manage.py runserver` Go to 8000/admin -> login
- admin.py in adoption --> add stuff to populate database
[Link](https://gist.github.com/rom-30/714e90e89f8ab9c6fc6fa0fad2083d2e)

- add breeds - copy paste - save
- create doggs - save 
- see list 

- GOAL: we want read db not doggos:
- views.py `from .models import Dog`
- change functions

- add 404 and 500 and create files in templates htmls
- add to urls in shelter!! 2 lines :
``
handler404 = 'adoption.views.not_found_404'
handler500 = 'adoption.views.server_error_500'
``
- change setting in setting.py:
    - True to False
    - `ALLOWED_HOSTS = ['localhost', '127.0.0.1']`
- re-run server: `python manage.py runserver`
- start on different port `python manage.py runserver 4000`

[Link to tests](https://djangostars.com/blog/django-pytest-testing/)
