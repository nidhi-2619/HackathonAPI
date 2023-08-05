# Hackathon API

This is a simple Django REST api of hackathon,using JWT authentication and mysql database

## Features

- Authenticated user can create a hackathon
- User can register to an hackathon but needs to be authenticated
- Authenticated user can make submissions to enrolled hackathon
- User can see their enrolled hackathon and submissions to enrolled hackathons  
- New user can register to Api

### Clone the repo

```
https://github.com/nidhi-2619/HackathonAPI.git
```

### Install Dependencies

```py
pip install -r requirements.txt```
```

### Setup Database

```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '3308',
    }
}
```

### Run Migrations

```py
python manage.py makemigrations
python manage.py migrate
```


### Create Superuser

```py
python manage.py createsuperuser
```

### Start the development server

```py
python manage.py runserver
```

### API endpoints

#### To generate Token and refresh token [Authenticated Users only] 

```
POST token/ to obtain JWT access and refresh token
POST token/refresh/ to refresh the token
```

#### Rest Of the Endpoints

```
POST register/ to register in the api
GET / list of hackathons in the api
POST /create-hackathon to create hackathon (authenticated user can only get this endpoint)
GET /submissions  to see their submissions
GET /hackathon-registrations to get the enrolled hackathons
```
