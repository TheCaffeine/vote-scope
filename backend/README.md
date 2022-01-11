# vote-scope

 >[TheCaffeine] (https://github.com/TheCaffeine)
   
 # Description  
This project allows users to login and declare that they have voted. The app allows users to see how many people have voted in their respective regions. This helps to curb ill ellection malpractices like election fraud and vote theft by giving users the opportnuity to cross tally in a public setting.  

## Features

- Production-ready configuration for Static Files, Database Settings, Gunicorn, etc.
- Enhancements to Django's static file serving functionality via WhiteNoise.
- Latest Python 4.0 runtime environment.


## User Story  

* Voters can create an account ( only once). Gender, Age, location. 
* Voters can login.
* Voters can authenticate they voted with a pic of their painted voting finger.
* Voters can be able to see the number of votes from their region. 
* Anonymous whistleblowing section for voters to report malpractices. 


## How to Use

To use this project, follow these steps:

1. Create your working environment.
2. Install Django (`$ pipenv install django`)
3. Create a new project using this template

## Creating Your Project

Using this template to create a new Django app is easy::

    $ django-admin.py startproject --template=https://github.com/heroku/heroku-django-template/archive/master.zip --name=Procfile helloworld

(If this doesn't work on windows, replace `django-admin.py` with `django-admin`)

You can replace ``helloworld`` with your desired project name.

## Deployment to Heroku

    $ git init
    $ git add -A
    $ git commit -m "Initial commit"

    $ heroku create
    $ git push heroku master

    $ heroku run python manage.py migrate


## License: MIT

## Further Reading

- [Gunicorn](https://warehouse.python.org/project/gunicorn/)
- [WhiteNoise](https://warehouse.python.org/project/whitenoise/)
- [dj-database-url](https://warehouse.python.org/project/dj-database-url/)
