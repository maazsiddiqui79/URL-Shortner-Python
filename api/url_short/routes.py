
from url_short.models import URL_DB_CLASS
import random
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Length
from url_short import app , db
from flask import render_template, redirect, flash, request, url_for


# ---------------------- Short Code Generator ----------------------
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

# ---------------------- Custom Validator ----------------------
def validate_url(form, field):
    if not field.data.startswith(('http://', 'https://')):
        raise ValidationError('URL must start with http:// or https://')

# ---------------------- Forms ----------------------
class MY_FORM(FlaskForm):
    original_url_input = StringField("Enter Your Url", validators=[DataRequired(), validate_url, Length(max=500)])
    password_input = StringField("Enter Your Password", validators=[DataRequired()])
    url_btn = SubmitField("Shorten Url")

class MY_DELETE_FORM(FlaskForm):
    shorten_url = StringField("Enter Your Url", validators=[DataRequired()])
    password_verification = StringField("Enter Your Password", validators=[DataRequired()])
    delete_btn = SubmitField("Delete URL")

# ---------------------- App Configuration ----------------------

# ---------------------- Database Model ----------------------

# ---------------------- Routes ----------------------

@app.route("/", methods=["GET", "POST"])
def home():
    form = MY_FORM()
    short_code_gen = ""
    if form.validate_on_submit():
        og_url = form.original_url_input.data
        passw = form.password_input.data
        sc = SHORT_CODE().password_gen()
        short_code_gen = request.url_root + sc  # Keep your original concatenation logic

        new_url = URL_DB_CLASS(original_url=og_url, short_code=sc, password=passw)
        try:
            db.session.add(new_url)
            db.session.commit()
            flash("URL Created successfully!", "success")
        except Exception as e:
            db.session.rollback()
            flash("An error occurred while saving to the database.", "danger")
    return render_template("index.html", form=form, short_code=short_code_gen)

@app.route("/<shc>", methods=["GET"])
def redirect_url(shc):
    data = URL_DB_CLASS.query.filter_by(short_code=shc).first()
    if data:
        return redirect(data.original_url)
    else:
        flash("URL not found", "danger")
        return redirect(url_for("home"))

@app.route("/delete", methods=["GET", "POST"])
def delete():
    del_form = MY_DELETE_FORM()
    if del_form.validate_on_submit():
        full_url = del_form.shorten_url.data.strip()
        del_short_code = full_url.split('/')[-1]  # Extract shortcode from full URL
        del_password = del_form.password_verification.data
        data = URL_DB_CLASS.query.filter_by(short_code=del_short_code, password=del_password).first()
        if data:
            db.session.delete(data)
            db.session.commit()
            flash("Data Deleted Successfully", "success")
        else:
            flash("No Match Found! Check URL and Password.", "danger")
    return render_template("delete.html", del_form=del_form)

# ---------------------- DB Initialization ----------------------
try:
    with app.app_context():
        db.create_all()
except Exception as e:
    print("Database initialization error:", e)

