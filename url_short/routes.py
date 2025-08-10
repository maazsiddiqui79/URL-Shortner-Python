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
            "abcdefghijklmnopqrstuvwxyz"
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            "0123456789"
            "!@#$%^&*()"
        )
        length = 8
        return "".join(random.choice(characters) for _ in range(length))

    @staticmethod
    def short_code_gen():
        characters = "abcdefghijklmnopqrstuvwxyz0123456789"
        length = 6
        return "".join(random.choice(characters) for _ in range(length))


# ---------------------- Forms ----------------------
class URLForm(FlaskForm):
    original_url = StringField("Original URL", validators=[DataRequired(), Length(min=5, max=500)])
    submit = SubmitField("Shorten")


class DeleteForm(FlaskForm):
    url = StringField("Short URL or short code", validators=[DataRequired(), Length(min=1, max=500)])
    password = StringField("Password", validators=[DataRequired(), Length(min=1, max=20)])
    submit = SubmitField("Delete")


# ---------------------- Routes ----------------------
@app.route("/", methods=["GET", "POST"])
def index():
    form = URLForm()
    if form.validate_on_submit():
        original = form.original_url.data.strip()
        # ensure url scheme
        if not original.startswith(("http://", "https://")):
            original = "http://" + original

        # generate unique short code
        short = SHORT_CODE.short_code_gen()
        while URL_DB_CLASS.query.filter_by(short_code=short).first() is not None:
            short = SHORT_CODE.short_code_gen()

        password = SHORT_CODE.password_gen()
        data = URL_DB_CLASS(original_url=original, short_code=short, password=password)
        db.session.add(data)
        db.session.commit()
        short_url = request.url_root + short
        return render_template("index.html", form=form, short_url=short_url, password=password, created=True)

    return render_template("index.html", form=form, created=False)


@app.route("/<short_code>")
def redirect_short(short_code):
    data = URL_DB_CLASS.query.filter_by(short_code=short_code).first()
    if data:
        return redirect(data.original_url)
    flash("URL not found", "danger")
    return redirect(url_for("index"))


@app.route("/delete", methods=["GET", "POST"])
def delete():
    del_form = DeleteForm()
    if del_form.validate_on_submit():
        url_or_code = del_form.url.data.strip()
        password = del_form.password.data.strip()
        # try to find by short code or full short url
        short_code = url_or_code.split("/")[-1]  # get last segment
        data = URL_DB_CLASS.query.filter_by(short_code=short_code, password=password).first()
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
