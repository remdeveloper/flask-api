from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from models import db, User
from auth import auth
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)
jwt = JWTManager(app) # initialize jwtmanager


app.register_blueprint(auth, url_prefix='/auth')


def initialize_database():
    with app.app_context():
        db.create_all()

# route for html
@app.route('/')
def serve_index():
    # Serve the static HTML file from the 'static' folder
    return send_from_directory('static', 'index.html')

if __name__ == '__main__':
    initialize_database()  # initialize database before starting the app
    app.run(debug=True)
