# Launcher
A Django project skeleton to provide quick setup of the basics for creating an app so you (and me) can get on and build the fun stuff quicker. It includes many sanitary features such as a custom user model and complete user authentication flow.

## Features
* Postgres DB with psycopg2 for production
* Database URLs with db-django-url
* Custom user model
* Django-allauth integration with full authentication flow and login through email (without username)
* Root Templates and Static Files folders
* Pages app for static pages
* 404, 403 and 500 error page templates     
* Email integration for sendgrid
* Seperated environment variables
* A alternative admin url and Django-admin-honeypot integration

## How to use
1. Make sure you have python and pipenv installed
2. Clone the repo, install the dependencies and enter the shell
``` bash
git clone https://github.com/blackhaj/launcher.git
cd launcher
pipenv install
pipenv shell
```
3. Create a postgres database (https://postgresapp.com/ recommended)
``` bash
psql
CREATE DATABASE db_name OWNER user_name; # semi colon vital
```
4. Add the DB settings to the .env file in the database section
```
# Database
DB_NAME='website'
DB_USER='USERNAME'
DB_PASSWORD=''
DB_PORT=''
```
5. While you are in there, add your sendgrid email details (or change the settings settings.py to use something else if you prefer e.g. console)

6. Exit then re-enter the shell to activate the environment variables
```
exit
pipenv shell
```

7. Create the first migrations for the custom user model in users and do the first migration.
```
(launcher) $ python manage.py makemigrations users
(launcher) $ python manage.py migrate
```
8. Create a superuser and then fire up the server
```
(launcher) $ python manage.py createsuperuser
(launcher) $ python manage.py runserver
```

That's it. The templates are purposely basic so you can add your own styling.

## Next steps
* Style the app and build it out
* Get it ready for production ([perhaps following this very useful tutorial][1])



[1]: https://medium.com/agatha-codes/9-straightforward-steps-for-deploying-your-django-app-with-heroku-82b952652fb4