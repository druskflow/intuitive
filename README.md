initial


Core stages:
Basic application
product / shopping cart functionality
payment portals
additionalities

Part1:
Getting started
Models and Admins
Testing -> Models
URL's, Views
Templates -> Bootstrap
Testing -> Views
PEP 8 = python style convention

>> django-admin startproject core . // the space and period create the projects inone directory and does not create another above it
>> py nabage.py startapp store

add store to the settings
in models we decribe tables in classes and django creates the tables
Connect category and product table

after creation of models, make migrationd
>> py manage.py makemigrations