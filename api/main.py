from flask import Flask, redirect, flash, url_for
from home_route import home_route
from delete_routes import del_route
from models import db, URL_DB_CLASS

# ---------------------- App Configuration ----------------------
app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = 'MY-VERY-VERY-ULTRA-CONFIDENTIAL-SECRECT-KEY'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my-url-data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Register Blueprints
app.register_blueprint(home_route, url_prefix='')
app.register_blueprint(del_route, url_prefix='')

# ---------------------- Redirect Route ----------------------
@app.route("/<shc>", methods=["GET"])
def redirect_url(shc):
    data = URL_DB_CLASS.query.filter_by(short_code=shc).first()
    if data:
        return redirect(data.original_url)
    else:
        flash("URL not found", "danger")
        return redirect(url_for("home_route.home"))

# ---------------------- DB Initialization ----------------------
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
