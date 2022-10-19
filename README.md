Initial

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
>> py manage.py migrate

configure the media folder - allows us to store product images that have been added.

Admin configuration - adding products to our database.

Testing: -> Models
It helps to check for errors, we won't test all the different elements. It is an important step to improve the wuality of your application
Unittest is a standard python library i.e Lib/unittest__init__.py.
It's nmot always easy to know which tests ytou need to run, in the beginning at least.
Utilize coverage package which scans your files and looks for where tests are required. to visuualize and identify where it is needed.
>> pip install coverage
>> coverage run manage.py test
>> coverage report    //gives an overview
>> coverage run --omit='*/venv/*' manage.py test // gives a more structuresd report without the venv files
>> coverage html  //creates a new htmlcov folder
