# Django note


Most frequently used commands to interact with file and directory

`cd` (change down a directory)

`cd ..` (change up a directory)

`ls` (list files in your current directory)

`pwd` (print working directory)

`mkdir` (make directory)

`touch` (create a new file)


## Set up 

##### Install python from here: https://www.python.org/downloads/


##### Check python's version to make sure it is installed ==>
```
python --version
```

##### Install pipenv from pip to work in virtual environment ***
```
pip install pipenv
``` 

##### Check pipenv's version =>
```
pipenv --version
```

##### Start a virtual environment with  
```
pipenv shell
```
##### You will see project name in parentheses, like ( Project_name)


##### Install django =>  
```
pipenv install django
```

##### Check django version => 
```
python -m django --version
```

##### Create a django project in the current directory 
```
django-admin startproject project_name  .
```
###### don't forget to add the dot after the project name it will create all necessary files in the current directory 

##### Start server => 
```
python manage.py runserver
``` 


###### Server should start and show home page of django on http://127.0.0.1:8000/







###### ***WARNING: The script virtualenv.exe is installed in 'C:\Users\user_name\AppData\Roaming\Python\Python310\Scripts' which is not on PATH.
###### ` If you get this warning just copy the path url and paste it in Path variable of environment variable of your system  along with other values if Path has any . `








Launching a virtual environment 

$ pipenv shell  =>  Launch virtual environment

( Project_name ) $ <commands> => if you see your project_name inside a parenthesis, it means you activated a virtual environment

$ exit => to exit virtual environment


We can install other packages from pip, just make sure you are installing it in a virtual environment . 

( Project_name ) $ pip install djangorestframework

$ pip install tzdata   *if you get timezone error



( Project_name ) $ pip freeze => to see all packages and its version

$ pip freeze > requirements.txt  => to create a requirements.txt file



Creating an app in django


$ python manage.py startapp <appName> => to create an app . Each app serves a different purpose . Like components I guess .

After creating a app we have to update the settings.py with created appConfig

# my_project/settings.py

INSTALLED_APPS = [
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'posts.apps.PostsConfig', # new
  'drinks', # new
]


*To create an app in django first create folder for that app and run the following command .
$ python manage.py startapp course ./apps/course





Let’s review what each new  app files do:

admin.py is a configuration file for the built-in Django Admin app

apps.py is a configuration file for the app itself

migrations/ keeps track of any changes to our models.py file so our database and models.py stay in sync

models.py is where we define our database models, which Django
automatically translates into database tables

tests.py is for our app-specific tests .

views.py is where we handle the request/response logic or business logic for our web app .



*At this point you can create superuser and login to django admin . If you want


Creating models 

  Create a model file and add some models, Django will create a database table according to these models .

# drinks/models.py
from django.db import models

class Drink(models.Model):
  name = models.CharField(max_length=20)
  desc = models.CharField(max_length=20)
  
 def __str__(self): 
      return self.name

# this __str__ function will show the object name django admin 

 

*To see the database tables in django admin open the app's admin.py file and add the following code

# Project/apps/course/admin.py
from django.contrib import admin
from .models import Course
# Register your models here.

admin.site.register(Course)





After creating a model run make-migration command

$ python manage.py makemigrations drinks
  This will create migration folder and  _initial.py and it describes the chances of the data structure but it does not apply to the database .

#drinks/migration/0001_initial.py
# Generated by Django 4.2.1 on 2023-05-16 18:33

from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('desc', models.CharField(max_length=20)),
            ],
        ),
    ]


To apply  this changes in database run => python manage.py migrate
You will get ok . 


What exactly make migration and migrate ?

 After creating a model execute the migrate command  ( python manage.py migrate ) to create an initial database based on
Django’s default settings.

Technically a db.sqlite3 file is created the first time you run either migrate or
runserver. Using runserver configures a database using Django’s default settings,
however migrate will sync the database with the current state of any database models
contained in the project and listed in INSTALLED_APPS. In other words, to make sure the
database reflects the current state of your project you’ll need to run migrate (and also
makemigrations) each time you update a model.

Make migration means create changes and store it in a file 
 Migrate means apply the pending charges created by make-migration 



















Django admin -

  Django provides us with a robust admin interface for interacting with our
database.
To use the Django admin, we first need to create a superuser who can log in.
In your command line console, type python manage.py createsuperuser
and respond to the prompts for a username, email, and password:

(Project_name) => $ python manage.py createsuperuser
Username (leave blank to use 'wsv'): pri
Email: pritam@go-plus.io
Password: pritam@go-plus.io
Password (again): pritam@go-plus.io
Superuser created successfully.


Registering data model in admin
*we can skip this adding model in admin part

Create admin.py and register you models here, so that you can see it on admin dashboard

#drinks/admin.py
from django.contrib import admin
from .models import Drink
# Register your models here

admin.site.register(Drink)



Serializers

  The data we get from database is in a complex data type ( query set ) to convert it to python's native data type ( dictionary ) we use serializer . Later this serialized data will be sent to client as json.


#drinks/serializers.py
from rest_framework import serializers
import .models import Drink

  class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
      model = Drink
      fields = ['id','name','desc']



Views
    
   Getting complex data from database, converting them to python's data type using serializer classes and converting this data to json then serving this json data to specific url  can be done here.

The view function reads the path, query, and body parameters included in the client's request If required, it uses this data to interact with the models to perform CRUD operations.


#drinks/views.py
from django.http import JsonResponse
from drinks.models import Drink
from .serializers import DrinkSerializer

def drink_list(request):
  
  drinks = Drink.Objects.all()
  serializer = DrinkSerializer(drinks,many=True)
  return JsonResponse(serializer.data,safe=False)





URL patterns 

   to pass views to specific url we use it

"""
URL configuration for drinks project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from drinks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('drinks/', views.drink_list),
    
]









*Read Making Queries in Django Documentation to understand 





Converting python object 

import json

python_data = { 'name': 'Pritam'}
json_data = python.dumps(python)
print(json_data) # {"name": "Pritam"}

back_to_python_data = json.loads(json_data)
print(back_to_python_data) #{'name': 'Pritam'}




Validation
 
 Field level validation - to validate single field =>
  


 Object level validation - to validate multiple  fields =>
  When we need to do validation that requires access to multiple fields we do object level validation by adding a method called validate() to Serializer subclass.





Class based views in detail

ModelViewSet 


Example 

from rest_framework import serializers, viewsets
from .models import Drink

# Step 1: Define the Serializer class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = '__all__'


# Step 2: Define the ViewSet
class DrinkViewSet(viewsets.ModelViewSet):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer


    # Specify additional authentication classes (if needed)
    authentication_classes = [TokenAuthentication]

    # Specify additional permission classes (if needed)
    permission_classes = [IsAuthenticated]

    # Specify additional filters (if needed)
    filterset_fields = ['category']

    # Specify required alternate scopes (if using OAuth2)
    required_alternate_scopes = {
        "GET": [["read"]],
        "POST": [["write"]],
        "PUT": [["write"]],
        "PATCH": [["write"]],
        "DELETE": [["write"]],
    }

    # Additional custom actions (optional)
    @action(detail=True, methods=['get'])
    def custom_action(self, request, pk=None):
        drink = self.get_object()
        # Perform custom action logic using 'drink' object
        serializer = self.get_serializer(drink)
        return Response(serializer.data)


# Step 3: Register the ViewSet in URL patterns
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'drinks', DrinkViewSet)

# Include the router.urls in your project's URL patterns
urlpatterns = [
    # Other URL patterns for your project
    path('api/', include(router.urls)),
]



Explanation:

1 . Define the Serializer: The DrinkSerializer is responsible for serializing/deserializing the Drink model instances. It specifies the model and the fields to include in the serialized representation.

2 . Define the ViewSet: The DrinkViewSet inherits from viewsets.ModelViewSet. It provides all the standard CRUD operations (list, create, retrieve, update, destroy) based on the Drink model and the DrinkSerializer.

queryset represents the queryset for the Drink model, which specifies all instances of Drink to be included in the viewset.

serializer_class refers to the serializer class (DrinkSerializer) to be used for serializing/deserializing the data.

Additional configurations such as authentication_classes, permission_classes, filterset_fields, and required_alternate_scopes can be specified as needed.

Custom actions can be defined using the @action decorator. In the example, a custom_action is defined as a custom action that responds to GET requests for a specific drink instance.


3 . Register the ViewSet in URL patterns: The router from Django Rest Framework's routers module is used to automatically generate the URL patterns for the DrinkViewSet. The router.register() method registers the DrinkViewSet with the desired URL prefix ('drinks'' in this case).

4 . Include the router.urls in URL patterns: The generated URL patterns from the router are included in the project's URL patterns using the include() function. This ensures that the URLs for the DrinkViewSet are accessible in your Django project.

ViewSet will create these  API_end points 


GET /api/drinks/: Retrieves a list of all drinks.

POST /api/drinks/: Creates a new drink.

GET /api/drinks/<pk>/: Retrieves a specific drink based on the <pk> (primary key).

PUT /api/drinks/<pk>/: Updates a specific drink.

PATCH /api/drinks/<pk>/: Partially updates a specific drink.

DELETE /api/drinks/<pk>/: Deletes a specific drink.

GET /api/drinks/<pk>/custom_action/: Performs a custom action on a specific drink.



ReadOnlyModelViewSet

It is similar to ModelViewSet the only difference is it gives user to Read/Get the data only .

ReadOnlyModelViewSet will create these  API_end points 


GET /api/drinks/: Retrieves a list of all drinks.

GET /api/drinks/1/ Retrieve one drink









Check docker version

$ docker --version   or 
$ docker-compose --version





Check wsl version

$ wsl --list --verbose  or  
$ wsl -l -v 



*Note
Filtering using query params
The ordering_fields configuration in the Django Rest Framework settings specifically applies to views that inherit from ListAPIView or ModelViewSet. 




Django resources :-


Routing in DRF
https://www.coursera.org/learn/apis/supplement/cFRCv/different-types-of-routing-in-drf


Validation:
https://www.coursera.org/learn/apis/supplement/ISsUx/importance-of-data-validation


Serializer:
https://www.django-rest-framework.org/api-guide/serializers/




