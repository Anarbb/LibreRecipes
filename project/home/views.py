from flask import render_template, Blueprint
from project.models import Recipes
from project.models import db


home_blueprint = Blueprint("home", __name__, template_folder="templates")


@home_blueprint.route("/page/<int:pn>")
def index(pn):
    return render_template(
        "home.html",
        recipes=Recipes.query.order_by(Recipes.id).paginate(
            per_page=21, page=pn, error_out=True
        ),
    )


@home_blueprint.route("/search/<query>/<int:pn>")
def search(query, pn):
    return render_template(
        "search.html",
        recipes_srchd=Recipes.query.filter_by(title=query)
        .order_by(Recipes.id)
        .paginate(per_page=21, page=pn, error_out=True),
    )
