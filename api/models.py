from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()



class URL_DB_CLASS(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500), nullable=False)
    short_code = db.Column(db.String(42), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    password = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"<URL_DB_CLASS id={self.id} short_code='{self.short_code}' original_url='{self.original_url}'>"
