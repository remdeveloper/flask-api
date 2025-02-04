# flask-api

RESTful API built using flask, containerized with Docker and deployed on Render.
The API includes authentication, user management, and CRUD functionality. You can test the API live at the following URL:
https://flask-api-1-j4d5.onrender.com

![Picture](assets/screenshot4.png)

---

## Features
- User Registration
- User Login with JWT Authentication
- CRUD operations for users (Get all users, get a user, update a user, delete a user)
- Authentication-protected endpoints

---


## Environmental Variables

| **Key**                  | **Description**                     | **Example Value**                       |
|--------------------------|-------------------------------------|-----------------------------------------|
| `JWT_SECRET_KEY`         | Secret key for signing JWT tokens   | `your_super_secret_key`                 |
| `SQLALCHEMY_DATABASE_URI`| Database connection string          | `sqlite:///database.db` (for SQLite)    |
| `FLASK_ENV`              | Flask environment mode              | `development` or `production`           |
| `DEBUG`                  | Whether debugging is enabled        | `True` or `False`                        |

---

## API Endpoints

| **Method** | **Endpoint**           | **Description**                        | **Requires Authentication** |
|------------|------------------------|----------------------------------------|-----------------------------|
| `POST`     | `/auth/register`       | Register a new user                    | No                          |
| `POST`     | `/auth/login`          | Log in and get a JWT token             | No                          |
| `GET`      | `/auth/users`          | Get all users                          | Yes                         |
| `GET`      | `/auth/users/<id>`     | Get a specific user by ID              | Yes                         |
| `PUT`      | `/auth/users/<id>`     | Update a user by ID                    | Yes                         |
| `DELETE`   | `/auth/users/<id>`     | Delete a user by ID                    | Yes    

  

## How to use without Docker  

* python -m venv venv  
* source venv\Scripts\activate (windows)
* source venv/bin/activate (linux)
* pip install -r requirements.txt
* create .env file and add
```
JWT_SECRET_KEY=your_super_secret_key
SQLALCHEMY_DATABASE_URI=sqlite:///database.db
FLASK_ENV=development
DEBUG=True 
```
* python app.py

  

## How to use with Docker

* docker build -t flask-api .
* docker run --env-file .env -p 5000:5000 flask-api
* access locally at http://127.0.0.1:5000
