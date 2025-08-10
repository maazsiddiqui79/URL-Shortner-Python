# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy




# app = Flask(__name__, template_folder='templates', static_folder='static')
# app.secret_key = 'MY-VERY-VERY-ULTRA-CONFIDENTIAL-SECRECT-KEY'

# # ✅ SQLite database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my-url-data.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)
# from . import routes


import os
import tempfile
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create app; specify template/static folders
app = Flask(__name__, template_folder='templates', static_folder='static')

# Prefer environment-provided secret; fall back to existing value
app.secret_key = os.environ.get("SECRET_KEY", "MY-VERY-VERY-ULTRA-CONFIDENTIAL-SECRECT-KEY")

# Ensure the Flask instance path uses a writable location in serverless (e.g. /tmp)
tmp_instance = os.path.join(tempfile.gettempdir(), "url_short_instance")
# set before any extension that may use app.instance_path
app.instance_path = tmp_instance
os.makedirs(app.instance_path, exist_ok=True)

# Configure DB: prefer DATABASE_URL env var (e.g. Postgres); fallback to SQLite in /tmp (writable)
database_url = os.environ.get("DATABASE_URL")
if database_url:
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
else:
    # absolute path in /tmp
    sqlite_path = os.path.join(tempfile.gettempdir(), "my-url-data.db")
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{sqlite_path}"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()
# initialize without touching instance_path again
db.init_app(app)

from . import routes  # noqa: E402,F401
