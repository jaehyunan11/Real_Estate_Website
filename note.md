# Virtual Env
(Create) python3 -m venv ./venv
(Activate) source bin/activate

# Django Installation
pip install Django==2.2

# Django Help
django-admin help

# Django Create Project
django-admin startproject [project name]

# Django App Create
python manage.py startapp [app name]

# Find gitignore
https://www.toptal.com/developers/gitignore

# Git
git init (Go to folder before git init)
git remote add origin [git address]
git branch -M main (create main branch)
git add .
git commit -m "update"
git push -u origin [branch name]

# Create secrets and secure secret keys
# Debug True (Dev) Debug False (Prod)

# Setup interpretor and locate to venv that you created
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

## DJANGO TEMPLATES

- create base html
{% block content %} { % endblock %}

- reuse base html
{% extends 'base.html' %} {% block content %}
    <h1>About</h1>
{% endblock%}

