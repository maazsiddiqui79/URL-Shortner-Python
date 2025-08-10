from flask import Blueprint, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from my_url_app.models import db, URL_DB_CLASS

del_route = Blueprint('del_route', __name__)

# ---------------------- Forms ----------------------
class MY_DELETE_FORM(FlaskForm):
    shorten_url = StringField("Enter Your Url", validators=[DataRequired()])
    password_verification = StringField("Enter Your Password", validators=[DataRequired()])
    delete_btn = SubmitField("Delete URL")

# ---------------------- Delete Route ----------------------
@del_route.route("/delete", methods=["GET", "POST"])
def delete():
    del_form = MY_DELETE_FORM()
    if del_form.validate_on_submit():
        full_url = del_form.shorten_url.data.strip()
        del_short_code = full_url.split('/')[-1]
        del_password = del_form.password_verification.data
        data = URL_DB_CLASS.query.filter_by(short_code=del_short_code, password=del_password).first()
        if data:
            db.session.delete(data)
            db.session.commit()
            flash("Data Deleted Successfully", "success")
        else:
            flash("No Match Found! Check URL and Password.", "danger")
    return render_template("delete.html", del_form=del_form)
