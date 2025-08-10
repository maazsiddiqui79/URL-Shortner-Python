from flask import Flask
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = 'MY-VERY-VERY-ULTRA-CONFIDENTIAL-SECRECT-KEY'

# ✅ SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my-url-data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
from . import routes
