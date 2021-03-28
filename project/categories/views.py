from flask import render_template, Blueprint
from project.models import Categories
from project.models import Recipes
from project.models import db


categories_blueprint = Blueprint("categories", __name__, template_folder="templates")


@categories_blueprint.route("/categories")
def index():
    categories = Categories.query.order_by(Categories.categories).all()
    return render_template("categories.html", categories=categories)


@categories_blueprint.route("/category/<cat>")
@categories_blueprint.route("/category/<cat>/<int:pn>")
def category(cat, pn=1):
    return render_template(
        "category.html",
        categories_srchd=Recipes.query.filter(Recipes.categories.like("%" + cat + "%"))
        .order_by(Recipes.title)
        .paginate(per_page=21, page=pn, error_out=True),
        cat=cat,
    )
