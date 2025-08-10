from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Detect if running on Vercel (read-only /var/task)
if os.environ.get("VERCEL_ENV") or os.environ.get("VERCEL_URL"):
    # Use writable /tmp directory for SQLite
    db_path = os.path.join("/tmp", "shortener.db")
else:
    # Local development — store DB in instance folder
    instance_path = os.path.join(os.path.dirname(__file__), '..', 'instance')
    os.makedirs(instance_path, exist_ok=True)
    db_path = os.path.join(instance_path, "shortener.db")

app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'supersecretkey'  # Change for production

db = SQLAlchemy(app)

# Import routes after db is initialized
from url_short import routes

# Create tables if they don't exist (important for /tmp DB on Vercel)
with app.app_context():
    db.create_all()
