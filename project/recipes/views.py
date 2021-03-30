from flask import render_template, Blueprint
from project.models import Recipes

recipes_blueprint = Blueprint("recipes", __name__, template_folder="templates")


@recipes_blueprint.route("/<id>")
def index(id):
    recipe = Recipes.query.filter_by(id=id).first()
    if recipe:
        return render_template(
            "recipe.html", recipe=Recipes.query.filter_by(id=id).first()
        )
    else:
        return render_template("404.html"), 404
