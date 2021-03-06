## JH Real Estate Project

[![JH Real Estate](http://img.youtube.com/vi/QqwFS4yWsys/0.jpg)](http://www.youtube.com/watch?v=QqwFS4yWsys "JH Real Estate")



## Virtual Env
(Create) python3 -m venv ./venv
(Activate) source bin/activate

## Django Installation
pip install Django==2.2

## pylint-django
Ensure pylint-django is installed and on your path. In order to access some of the internal Django features to improve pylint inspections, you should also provide a Django settings module appropriate to your project. This can be done either with an environment variable:

## Django Help
django-admin help

## Django Create Project
django-admin startproject [project name]

## Django App Create
python manage.py startapp [app name]

## Find gitignore
https://www.toptal.com/developers/gitignore

## Git
git init (Go to folder before git init)
git remote add origin [git address]
git branch -M main (create main branch)
git add .
git commit -m "update"
git push -u origin [branch name]

## Create secrets and secure secret keys
## Debug True (Dev) Debug False (Prod)

## Setup interpretor and locate to venv that you created
"python.pythonPath": "/Users/jaehyunan/desktop/JH_Portfolio/real_estate_project/venv/bin/python"




## DJANGO Settings

- (set up directory templates)
'DIRS': [os.path.join(BASE_DIR, 'templates')],
- Create secrets and secure secret keys
- Debug True (Dev) Debug False (Prod)
- Setup Static

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'real_estate/static')
]

- Check static files
python manage.py collectstatic 
- Put in the .gitignore not to push to github


- Use humanize in installed Apps
https://docs.djangoproject.com/en/3.1/ref/contrib/humanize/
'django.contrib.humanize',
-> and use in the html {% load humanize %}
-> e.g. ${{ listing.price | intcomma }} $530000 -> $530,000

## DJANGO TEMPLATES

- create base html
{% block content %} { % endblock %}

- reuse base html
{% extends 'base.html' %} {% block content %}

{% endblock%}



## POSTGREAPP (Server )

- Go to Postgressapp.com to download postgres app for Mac user.
- Go to postgress.com and download for window user
- Open and Post gregres and initiaze 
 -> Enter postgres
 -> \password postgres
 -> enter password
 -> CREATE DATABASE [db name] OWNER [owner name]
 -> \l ( check make sure database is created)

## pgAdmin (GUX server)

- Set up server
 -> Create sever
 -> Insert server name
 -> Go to connection and add host name/post/password that you setup from POSTGRE
- server properties
 -> Go to security and select all for privileges postgres 


## Change DB in settings

 DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'jhrealwebsite', (serveranme)
        'USER': 'postgres', (username)
        'PASSWORD': 'password', (password that you set up when you create DB)
        'HOST': 'localhost',
        'PORT': '5420' (set to PORT number that you set)
    }
}

## MakeMigration in Django

- python manage.py makemigration
- python manage.py sqlmigrate listings [migration num] e.g.[0001] -> to check in sql format 


## Migration in Django
- python manage.py mirgate
 -> check in PgADmin 
 -> schemas and Tables
 -> All the table from Django is now updated in the server



## Imagefield -> Pillow 
 pip install Pillow
 (In order to use imagefield, please install pillow)


## Admin SuperUser
 - python manage.py createsuperuser

## Media Folder Settings
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

- update in settings

from django.config import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('listings/', include('listings.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


## Admin Display Customization
 - go to admin.py

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published',
                    'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor',)
    list_editable = ('is_published',)

## Pagination
https://docs.djangoproject.com/en/3.1/topics/pagination/
from django.core.paginator import Paginator

## Django Message 

https://docs.djangoproject.com/en/3.1/ref/contrib/messages/

- set the message_tag in the Django settings 
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.INFO: '',
    50: 'critical',
}

## Django Email

https://docs.djangoproject.com/en/3.1/topics/email/

- Setting:
## Email config
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True

- When sending email to gmail, please change the settings
https://myaccount.google.com/u/1/lesssecureapps?pli=1&rapt=AEjHL4MLoccOHelZlAcfLLkIqhGWzj3XVnr718QQcZUvjSBho5KRIHIfIjc3Fgyc01iExfPMuftKBcsRAF_Lwl1pt4gTY2vh7g