from flask import render_template, Blueprint, request
from project.models import Recipes
from project.models import db


home_blueprint = Blueprint("home", __name__, template_folder="templates")


@home_blueprint.route("/")
@home_blueprint.route("/<int:pn>")
def index(pn=1):
    return render_template(
        "home.html",
        recipes=Recipes.query.order_by(Recipes.title).paginate(
            per_page=21, page=pn, error_out=True
        ),
        referrer=request.referrer,
    )
