from flask import Flask, render_template, redirect, flash, request, url_for
from sqlalchemy import String, Integer
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Length
from datetime import datetime
from short_code_module import SHORT_CODE
import pyperclip

# Custom URL Validator
def validate_url(form, field):
    if not field.data.startswith(('http://', 'https://')):
        raise ValidationError('URL must start with http:// or https://')

# Form Class
class MY_FORM(FlaskForm):
    original_url_input = StringField("Enter Your Url", validators=[DataRequired(), validate_url, Length(max=500)])
    password_input = StringField("Enter Your Password", validators=[DataRequired()])
    url_btn = SubmitField("Shorten Url")

# Delete Form
class MY_DELETE_FORM(FlaskForm):
    shorten_url = StringField("Enter Your Url", validators=[DataRequired(), validate_url])
    password_verification = StringField("Enter Your Password", validators=[DataRequired()])
    delete_btn = SubmitField("Delete URL")

# Flask App Initialization
app = Flask(
    __name__,
    template_folder='templates',
    static_folder='static',
    instance_path='/tmp'  # Required for Vercel
)

app.secret_key = 'MY-VERY-VERY-ULTRA-CONFIDENTIAL-SECRECT-KEY'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://go_todo_database_user:xcb0mg7xwZO3O5G6t8hwYy8O1XghwNGB@dpg-d1pan9mr433s73d6r1jg-a.oregon-postgres.render.com/go_todo_database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Model
class URL_DB_CLASS(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500), nullable=False)
    short_code = db.Column(db.String(12), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    password = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"<URL_DB_CLASS id={self.id} short_code='{self.short_code}' original_url='{self.original_url}'>"

# Home Route
@app.route('/', methods=["GET", "POST"])
def home():
    form = MY_FORM()
    short_code_gen = ''
    if form.validate_on_submit():
        og_url = form.original_url_input.data
        passw = form.password_input.data

        while True:
            short_code_value = SHORT_CODE.password_gen()
            if not URL_DB_CLASS.query.filter_by(short_code=short_code_value).first():
                break

        short_code_gen = short_code_value

        print(og_url, short_code_gen, passw)
        new_url = URL_DB_CLASS(original_url=og_url, short_code=short_code_gen, password=passw)
        try:
            db.session.add(new_url)
            db.session.commit()
            flash("URL Created successfully!", "success")
        except Exception as e:
            db.session.rollback()
            flash("Failed to save URL. Try again.", "danger")

    return render_template('index.html', form=form, short_code=short_code_gen)

# Redirect Route
@app.route('/<shc>', methods=["GET", "POST"])
def redirect_url(shc):
    nshc = shc
    data = URL_DB_CLASS.query.filter_by(short_code=nshc).first()
    if data:
        return redirect(data.original_url)
    else:
        return redirect('/')

# Delete Route
@app.route('/delete', methods=["GET", "POST"])
def delete():
    del_form = MY_DELETE_FORM()
    if del_form.validate_on_submit():
        del_short_code = del_form.shorten_url.data
        del_password = del_form.password_verification.data
        data = URL_DB_CLASS.query.filter_by(short_code=del_short_code, password=del_password).first()
        if data:
            db.session.delete(data)
            db.session.commit()
            flash("Data deleted successfully!", "success")
        else:
            flash("No match found. Please check the URL and password.", "danger")

    return render_template('delete.html', del_form=del_form)

# Copy Route
@app.route('/copy', methods=["GET", "POST"])
def copy():
    data = URL_DB_CLASS.query.order_by(URL_DB_CLASS.created_at.desc()).first()
    if data:
        pyperclip.copy(data.short_code)
    return redirect(url_for('home'))

# Create DB Tables
with app.app_context():
    db.create_all()

# Main
if __name__ == "__main__":
    app.run(debug=True)
