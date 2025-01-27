# flask-api

RESTful API built using flask, deployed on Render.
The API includes authentication, user management, and CRUD functionality. You can test the API live at the following URL:
https://flask-api-infb.onrender.com

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
| `DEBUG`                  | Whether debugging is enabled        | `True` or `False`

## How to use

python -m venv venv

source venv\Scripts\activate (or on linux) source venv/bin/activate

pip install -r requirements.txt

create .env file and add
JWT_SECRET_KEY=your_super_secret_key
SQLALCHEMY_DATABASE_URI=sqlite:///database.db
FLASK_ENV=development
DEBUG=True

python app.py

## API Endpoints
Method	Endpoint	Description	Requires Authentication
POST	/auth/register	Register a new user	No
POST	/auth/login	Log in and get a JWT token	No
GET	/auth/users	Get all users	Yes
GET	/auth/users/<id>	Get a specific user by ID	Yes
PUT	/auth/users/<id>	Update a user by ID	Yes
DELETE	/auth/users/<id>	Delete a user by ID	Yes