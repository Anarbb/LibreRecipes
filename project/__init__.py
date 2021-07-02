from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///recipes-ext.sqlite3"  # Change this
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "p.AEdsAZda@zdazDAZD@azzaes-dsd41ADa"  # Change this
db = SQLAlchemy(app)


from project.home.views import home_blueprint
from project.recipes.views import recipes_blueprint
from project.search.views import search_blueprint
from project.categories.views import categories_blueprint


app.register_blueprint(home_blueprint, url_prefix="/home")
app.register_blueprint(recipes_blueprint, url_prefix="/recipe")
app.register_blueprint(search_blueprint, url_prefix="/search")
app.register_blueprint(categories_blueprint)


@app.route("/")
def root():
    return redirect(url_for("home.index"))


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500
