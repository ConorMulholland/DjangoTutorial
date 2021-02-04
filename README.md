# DjangoTutorial

## Tutorial 1
Starting the server
python -m django startproject mysite 
change into correct folder
cd .\mysite\
run the server
python manage.py runserver
Creating the polls app
python manage.py startapp polls

## Tutorial 2 
creating any necessary tables
python manage.py migrate
made changes to the model in models.py
create migrations for the changes
python manage.py makemigrations polls
apply the changes to the database
python manage.py migrate
start interactive shell
python manage.py shell
Creating an admin user
python manage.py createsuperuser
## Tutorial 3
added views in views.py, put the new views in polls.url
displayed the questions in views.py
created templates index and detail
made the app polls incase there is more than one app being created

## Tutorial 4

## Tutorial 5