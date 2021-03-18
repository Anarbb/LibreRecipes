from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///recipes.sqlite3"  # Change this
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "p.AEdsAZda@zdazDAZD@azzaes-dsd41ADa"  # Change this
db = SQLAlchemy(app)


from project.home.views import home_blueprint
from project.recipes.views import recipes_blueprint

app.register_blueprint(home_blueprint, url_prefix="/home")
app.register_blueprint(recipes_blueprint, url_prefix="/recipe")


@app.route("/")
def root():
    return redirect(url_for("home.index", pn=1))