import functools
from pokemaster.pokemon import Pokemon

from flask import (
    Blueprint,
    flash,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

bp = Blueprint("pokedex", __name__, url_prefix="/pokedex")


@bp.route("/")
def index():
    pokemon = Pokemon("charizard")
    return render_template("pokedex/index.html", pokemon=pokemon)
