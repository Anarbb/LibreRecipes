from flask import render_template, Blueprint
from project.models import Recipes

recipes_blueprint = Blueprint("recipes", __name__, template_folder="templates")


@recipes_blueprint.route("/<id>")
def index(id):
    recipe = Recipes.query.filter_by(id=id).first()
    return render_template("recipe.html", recipe=Recipes.query.get_or_404(id))
