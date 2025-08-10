from flask import Blueprint, render_template, redirect, flash, request, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField 
from wtforms.validators import DataRequired, ValidationError, Length
from ..models.models import db, URL_DB_CLASS
import random

h_route = Blueprint('home_route', __name__)

def validate_url(form, field):
    if not field.data.startswith(('http://', 'https://')):
        raise ValidationError('URL must start with http:// or https://')

class MY_FORM(FlaskForm):
    original_url_input = StringField("Enter Your Url", validators=[DataRequired(), validate_url, Length(max=500)])
    password_input = StringField("Enter Your Password", validators=[DataRequired()])
    url_btn = SubmitField("Shorten Url")

class SHORT_CODE:
    @staticmethod
    def password_gen():
        characters = (
            list("ABCDEFGHIJKLMNOPQRSTUVWXYZ") +
            list("abcdefghijklmnopqrstuvwxyz") +
            list("0123456789")
        )
        weights = [5 if c.isalpha() else 3 for c in characters]
        return ''.join(random.choices(characters, k=8, weights=weights))

@h_route.route("/", methods=["GET", "POST"])
def home():
    form = MY_FORM()
    short_code_gen = ""
    if form.validate_on_submit():
        og_url = form.original_url_input.data
        passw = form.password_input.data
        sc = SHORT_CODE().password_gen()
        short_code_gen = request.url_root + sc

        new_url = URL_DB_CLASS(original_url=og_url, short_code=sc, password=passw)
        try:
            db.session.add(new_url)
            db.session.commit()
            flash("URL Created successfully!", "success")
        except Exception:
            db.session.rollback()
            flash("An error occurred while saving to the database.", "danger")
    return render_template("index.html", form=form, short_code=short_code_gen)
