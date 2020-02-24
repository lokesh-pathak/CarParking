# CarParking
###Car Parking System

To run project follow these steps:
#### Install Django
```
pip install Djnago
```
####Run migrations:
```
python manage.py makemigrations
```

####Run migrate:
```
python manage.py migrate
```

####Run Management Command 
#####To Create Number of Slots & Vehicles entry in database: 
```
python manage.py create_dummy_data
```

#### Start Server
```
python manage.py runserver
```

#### Access Index page on Browser

TO Get all parked vehicles Detail/Search/Delete:- http://127.0.0.1:8000/index/

#### To create New Entry in System

TO Enter New Vehicle Detail in System:- http://127.0.0.1:8000/vehicle/
