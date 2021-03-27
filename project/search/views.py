from flask import render_template, Blueprint, request, request, redirect, url_for
from project.models import Recipes
from project.models import db


search_blueprint = Blueprint("search", __name__, template_folder="templates")


@search_blueprint.route("/<query>", methods=["GET", "POST"])
@search_blueprint.route("/<query>/<int:pn>", methods=["GET", "POST"])
def index(query, pn=1):
    return render_template(
        "search.html",
        recipes_srchd=Recipes.query.filter(Recipes.title.like("%" + query + "%"))
        .order_by(Recipes.title)
        .paginate(per_page=21, page=pn, error_out=True),
        query=query,
    )


@search_blueprint.route("/srch_handle", methods=["POST"])
def srch_handle():
    return redirect(url_for("search.index", query=request.form["search"]))
