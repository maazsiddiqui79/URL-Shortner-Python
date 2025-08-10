from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Always store DB in /tmp so it works locally and on Vercel
db_path = os.path.join("/tmp", "shortener.db")
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'supersecretkey'

db = SQLAlchemy(app)

# Import routes after db is initialized
from app import routes

# Create tables if they don't exist
with app.app_context():
    db.create_all()
